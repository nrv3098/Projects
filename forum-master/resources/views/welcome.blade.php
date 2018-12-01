


<!doctype html>
<html lang="{{ app()->getLocale() }}">
    <head>
        
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>AskTech Forum</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet" type="text/css">

        <!-- Styles -->
        <style>
            html, body {
                background-image: url(/bg3.jpg);
                background-color: #fff;
                color: #636b6f;
                font-family: 'Nunito', sans-serif;
                font-weight: 200;
                height: 100%;
                margin: 0;
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }

            .full-height {
                height: 100%;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                color: white;
                text-align: center;
            }

            .title {
                font-size: 100px;
            }

            .links > a {
                color: white;
                padding: 0 25px;
                font-size: 20px;
                font-weight: 600;
                letter-spacing: .1rem;
                text-decoration: none;
                text-transform: uppercase;
                
            }

            .m-b-md {
                margin-bottom: 30px;
            }

            button{
                background-color: white;
                color: grey;
                position: relative;
                top: 20px;
                left: -50px;

            }
           
}
            

        </style>
    </head>
    
        
        <div class="flex-center position-ref full-height">
            @if (Route::has('login'))
                <div class="top-right links">
                    @auth
                        <a href="http://localhost:8000">Home</a>
                        <a href="http://localhost:8000/forums">Forum</a>
                    @else
                        <a href="http://localhost:8000/forums">Forum</a>
                        <a href="{{ route('login') }}">Login</a>
                        <a href="{{ route('register') }}">Register</a>
                        
                    @endauth
                </div>
            @endif

            <div class="content">
                <div class="title m-b-md">
                    AskTech Forum
                </div>

                <div class="links">
                    <a href="http://localhost:8000/forums">Go to Forum</a>
                </div>
            </div>
        </div>
    </body>
</html>
