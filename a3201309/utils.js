function validate_login(){
        var email = document.getElementById('email_field').value;
        var pword = document.getElementById('pword_field').value;
        var data = {table: "SELECT * FROM Student", condition: email, column: "Email"};
        $.ajax({
          data : data,
          url : 'run_query.php',
          type : "GET",
          dataType : "json"}).done(function(result){
            if(result.length == 0){
              document.getElementById('error_space').innerHTML = 'This Email is not registered for MyPy</br>You can Sign Up Now';
            }
            else{
              for(x = 0; x < result.length; x++){
                if(result[x]['Password'] == pword){
                  var login_details = {id: result[x]['StudentID'], type:"student"};
                  $.ajax({
                    data:login_details,
                    url: 'set_sessions.php',
                    type: 'GET',
                    dataType: "",
                    success: function(html){
                      window.location.assign('userPage.php');
                    }
                  });
                }
                else{
                  document.getElementById('error_space').innerHTML = 'Password incorrect';
                }
              }
            }
          });
        }