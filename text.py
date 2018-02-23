dockerfile = """FROM 391292943957.dkr.ecr.ap-southeast-1.amazonaws.com/warrior/tomcat:2.0

ENV PROJECT ******

ADD ./$PROJECT.war /usr/local/webapps/$PROJECT.war"""
