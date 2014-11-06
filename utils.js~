function validate_login(type_of_user){
        var email = document.getElementById('email_field').value;
        var pword = document.getElementById('pword_field').value;
        var data = {table: "SELECT * FROM "+type_of_user, criterion: email, column: "Email"};
        $.ajax({
          data : data,
          url : 'https://web.cs.manchester.ac.uk/mbax9zh2/thirdyearproject/run_query.php',
          type : "GET",
          dataType : "json"}).done(function(result){
            if(result.length == 0){
              document.getElementById('error_space').innerHTML = 'This Email is not a registered MyPy '+ type_of_user +'</br>You can Sign Up Now';
            }
            else{
              for(x = 0; x < result.length; x++){
                if(result[x]['Password'] == pword){
                  var login_details = {id: result[x][type_of_user.charAt(0).toUpperCase()+type_of_user.splice(1)+'ID'], type:type_of_user};
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
