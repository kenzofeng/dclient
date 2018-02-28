dockerfile = """FROM 391292943957.dkr.ecr.ap-southeast-1.amazonaws.com/warrior/tomcat:2.0<br>
<br>
ENV PROJECT <span style=' color:#ff0000;'>YOUR_PROJECT_NAME</span><br>
<br>
ADD ./$PROJECT.war /usr/local/webapps/$PROJECT.war"""
