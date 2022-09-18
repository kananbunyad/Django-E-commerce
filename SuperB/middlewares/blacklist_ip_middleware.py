from django.core.exceptions import PermissionDenied
from django.utils.deprecation import MiddlewareMixin
from django.http import Http404
from django.http import HttpResponse

class BlackListIPMiddleware(MiddlewareMixin):
    BLACK_IP_LIST = [
        # '127.0.0.1'
        
    ]


    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))
        if request.META.get('REMOTE_ADDR') in self.BLACK_IP_LIST:
            

            html = """
        <!DOCTYPE html>
            <html lang="en">
            <title>BLOCKED!!!</title>
            <link rel="shortcut icon" type="image/png" href="https://cdn.pixabay.com/photo/2021/10/10/04/03/prohibited-6695541_960_720.png" />
            <body>
                <br><br><br><br><br><br><br><br><br>
                <div style="text-align: center;">
                    <img src="https://static.thenounproject.com/png/977866-200.png" alt="No image!!!" style="height: 250px;">
                    <h1>Your IP adress blocked!!!</h1>
                
                    <p style="font-size:15px;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus id natus nulla optio praesentium odit, beatae porro tenetur esse quod illo?<br> Amet laborum repellendus quia. Aspernatur necessitatibus cumque ratione beatae?<br>
                    at, porro optio amet, praesentium officiis pariatur soluta, aliquid ea quibusdam consequuntur totam.</p>
                    <button type="button" style="
                    background-color:#C2A476;
                    color:white;
                    width:150px;
                    height:40px;
                    border-radius:10px;
                    cursor:pointer;
                    text-size:25px;
                    " 
                    onclick="alert('Sorry you ip addres blocked!')">Notify Admin</button>
                </div>
            </body>
            </html>
            """

            action = request.GET.get('action', '')
            if action == 'raise403':
                raise PermissionDenied
            elif action == 'raise404':
                raise Http404
            elif action == 'raise500':
                raise Exception('Server error')

            return HttpResponse(html)