swampdragon.subscribe('notifications', 'messages', null, function(context, data) {
    console.log(context, data)
});

swampdragon.onChannelMessage(function (channels, message) {
            createMessageElement('<strong>' +
                                 message['data']['ts_created']+ ' ' +
                                 message['data']['text'] +
                                 '</strong>')
});


function createMessageElement(text) {
  var ul = document.getElementById('messages_list');
  var li = document.createElement('li');
  li.innerHTML = text;
  li.setAttribute("class", "list-group-item");
  ul.insertBefore(li, ul.firstChild);
}