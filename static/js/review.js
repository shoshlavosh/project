$("document").ready( //listens for when the document has loaded all the DOM elements
                    //makes it possible to take script tag from bottom of html document and move it into the head of the html document
$('#review').on('submit', (evt) => {    //listening for the "review" id. On a submit event, use this handler
                                        //event is created when submit button is clicked
    evt.preventDefault(); //because default behavior of a form is to trigger a redirect or refresh

  const route = evt.target.getAttribute("data-route"); //the form is the target, uses getAttribute to get the value of "data-route"
  const data = {"review_text" : $("#review_text").val(),
                "landlord_name" : $("#landlord_name").val()}; //json object with name as the key, and value with the review_text id

  $.post(route, data, (res) =>{ //first argument is the route pulled out of data-route, second argument is key/value pairs for the query string
    //third argument is the function that handles the response from the first argument route
    $("#reviews").append(res); 
    $("#review_text").val(""); //this empties the form afterwards
    $("#landlord_name").val(""); //empties this part of the form as well
    // console.log($("#reviews"));
    // console.log(res);
  }); 
})   
);