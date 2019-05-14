// import $ from "jquery";
// $(document).ready(function () {
//     $('#datetimepicker1').datetimepicker();
//     // $('#datetimepicker1').datepicker();
// });
//

$(document).ready(function () {

// jQuery(document).ready(function(){
//
// var $ = jQuery;
// jQuery(document).ready(function($){

    // Correctly decide between ws:// and wss://
    // var ws_path = 'ws://' + window.location.host + '/chat/chat/';
    var roombackid;
    var roombackclose;
    var ws_path = '/chat/stream/';
    console.log("Connecting to " + ws_path);
    var webSocketBridge = new channels.WebSocketBridge();
    webSocketBridge.connect(ws_path);
    // Handle incoming messages

    webSocketBridge.listen(function (data) {
        // Decode the JSON
        console.log("Got websocket message", data);
        // Handle errors

        if (data.error) {
            alert(data.error);
            return;
        }
        var curuser = $(".chat-avatar")[0].id;
        var chatuser = "";
        // Handle joining
        if (data.join) {
            console.log("Joining room " + data.join);

            var sendmes = $(".aside-chat-box");
            var roomdiv = $(
                "<div class='conversation-container' id='room-" + data.join + "'>" +
                "</div>");
            // $("#chats").append(roomdiv);
            $("#chattitle").find(".chat-user-status")[0].innerHTML = data.title;
            // $(".chat-user-status")[0].innerHTML = data.title;
            // Hook up send button to send a message

            sendmes.find("#chat-input").on("keydown", function () {
                flag = $("#chat-input")[0].value.length;
            });
            sendmes.find("#chat-input").on("keyup", function (e) {
                if (e.keyCode === 13) {
                    if ($("#chat-input")[0].value.length !== flag) {
                        return;
                    }
                    else
                        webSocketBridge.send({
                            "command": "send",
                            "room": roomId,
                            // "room": data.join,
                            "message": sendmes.find("input").val()
                        });
                        sendmes.find("input").val("");
                        return false;
                }
                // Handle leaving
            });
            $("#chats").append(roomdiv);
        }
        else if (data.leave) {
            console.log("Leaving room " + data.leave);
            document.getElementById("room-" + data.leave).remove();
            // $("#room-" + data.leave).remove();
            // var div = document.getElementById("room-" + data.leave);
            // div.parentNode.removeChild(div);
            // Handle getting a message
        } else if (data.message || data.msg_type !== 0) {
            var msgdiv = $("#room-" + data.room);
            // var msgdiv = $("#room-" + data.room + " .conversation-list");
            var ok_msg = "";
            chatuser = data.username;
            // console.log(chatuser);
            // msg types are defined in chat/settings.py
            // Only for demo purposes is hardcoded, in production scenarios, consider call a service.
            switch (data.msg_type) {
                case 0:
                    // Message
                    // ok_msg = "<div >" +
                    //     "<span class='username'>" + data.username + ": </span>" +
                    //     "<span class='body'>" + data.message + "</span>" +
                    //     "</div>";
                    // console.log(curuser + " === " + chatuser);

                    // ok_msg = "<li>" +
                    //     "<p><span class='body'>" + data.message + "</span></p>" +
                    //     "</li><br>";
                    if (curuser === chatuser) {
                        // console.log("равно");
                        ok_msg = $(
                            "<div class='conversation-row even' >" +
                            "<ul class='conversation-list' >" +
                            "<li>" +
                            "<p><span class='body'>" + data.message + "</span></p>" +
                            "</li><br>" +
                            "</ul>" +
                            "</div>")
                    }
                    else {
                        // console.log("не равно");
                        ok_msg = $(
                            "<div class='conversation-row odd' >" +
                            "<ul class='conversation-list' >" +
                            "<li>" +
                            "<p><span class='body'>" + data.message + "</span></p>" +
                            "</li><br>" +
                            "</ul>" +
                            "</div>" +
                            "</div>")
                    }

                    break;
                case 1:
                    // Warning / Advice messages
                    // ok_msg = "<div class='contextual-message text-warning'>" + data.message +
                    //     "</div>";
                    ok_msg =
                        "<div class='conversation-row odd' >" +
                        "<ul class='conversation-list' >" +
                        "<li>" +
                        "<p><div class='contextual-message text-warning'>" + data.message + "</div></p>" +
                        "</li><br>" +
                        "</ul>" +
                        "</div>";

                    break;
                case 2:
                    // Alert / Danger messages
                    // ok_msg = "<div class='contextual-message text-danger'>" + data.message +
                    //     "</div>";
                    ok_msg =
                        "<div class='conversation-row odd' >" +
                        "<ul class='conversation-list' >" +
                        "<li>" +
                        "<p><div class='contextual-message text-danger'>" + data.message + "</div></p>" +
                        "</li><br>" +
                        "</ul>" +
                        "</div>";

                    break;
                case 3:
                    // "Muted" messages
                    // ok_msg = "<div class='contextual-message text-muted'>" + data.message +
                    //     "</div>";
                    ok_msg =
                        "<div class='conversation-row odd' >" +
                        "<ul class='conversation-list' >" +
                        "<li>" +
                        "<p><div class='contextual-message text-muted'>" + data.message + "</div></p>" +
                        "</li><br>" +
                        "</ul>" +
                        "</div>";
                    break;
                case 4:
                    // User joined room
                    // ok_msg = "<div class='contextual-message text-muted'>" + data.username +
                    //     " joined the room!" +
                    //     "</div>";
                    ok_msg =
                        "<div class='conversation-row odd' >" +
                        "<ul class='conversation-list' >" +
                        "<li>" +
                        "<p><div class='contextual-message text-muted'>" + data.username + " joined the room!</div></p>" +
                        "</li><br>" +
                        "</ul>" +
                        "</div>";
                    break;
                case 5:
                    // User left room
                    // ok_msg = "<div class='contextual-message text-muted'>" + data.username +
                    //     " left the room!" +
                    //     "</div>";
                    ok_msg =
                        "<div class='conversation-row odd' >" +
                        "<ul class='conversation-list' >" +
                        "<li>" +
                        "<p><div class='contextual-message text-muted'>" + data.username + " left the room!</div></p>" +
                        "</li><br>" +
                        "</ul>" +
                        "</div>";
                    break;
                default:
                    console.log("Unsupported message type!");
                    return;
            }
            msgdiv.append(ok_msg);
            msgdiv.scrollTop(msgdiv.prop("scrollHeight"));
        } else {
            console.log("Cannot handle message!");
        }
    });
    // Says if we joined a room or not by if there's a div for it
    inRoom = function (roomId) {
        return $("#room-" + roomId).length > 0;
    };
    // Room join
    $("li.chat-u-online").click(function () {
        roomId = $(this).attr("data-room-id");
        roombackclose = $(this);
        roombackid = roomId;
        // Join room
        $(this).addClass("joined");
        webSocketBridge.send({
            "command": "join",
            "room": roomId
        });
    });
    // Room leave
    $("#chatback").click(function () {
        roomId = roombackid;
        $(roombackclose).removeClass("joined");
        webSocketBridge.send({
            "command": "leave",
            "room": roomId
        });
    });
    // Helpful debugging
    webSocketBridge.socket.onopen = function () {
        console.log("Connected to chat socket");
    };
    webSocketBridge.socket.onclose = function () {
        console.log("Disconnected from chat socket");
    }
});
