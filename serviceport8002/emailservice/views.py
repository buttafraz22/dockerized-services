from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail, BadHeaderError
from .serializers import EmailSerializer
from .models import Email
from django.http import JsonResponse
from .publisher import *



# Create your views here.

class SendEmailAPIView(APIView):
    def post(self, request):

        # Message Broking Logic. Communicate with the Users Service over localhost,
        # Hereby Validating the Entire Request Parsing Logic. Previously, I did this 
        # through a manual monolithic import statement.

        # headers_dict = {key: value for key, value in request.headers.items()}
        # user = send_auth(headers_dict)
        # print(user)
        publish(request.data)
        serializer = EmailSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        subject = serializer.validated_data['subject']
        content = serializer.validated_data['content']
        recipient = serializer.validated_data['recipient']
        message = serializer.validated_data['message'] or " "

        if type(recipient) != type(list):
            recipient = [recipient]

        if not subject or not content or not recipient:
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        if message and len(message) > 2000:
            return Response(serializer.errors, status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

        try:
            SENDER_USERNAME = 'afraz.jed.grw@gmail.com'

            Email.objects.create(   content=content,
                                    subject=subject, 
                                    sender_username=SENDER_USERNAME, 
                                    sent_to=recipient,
                                    )

            send_mail(subject=subject,message=message if message else '', from_email=SENDER_USERNAME, recipient_list=recipient, html_message=content)
        except BadHeaderError:
            return Response({'message' : 'Header Injection Attempted. Aborting Email operation.'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)


