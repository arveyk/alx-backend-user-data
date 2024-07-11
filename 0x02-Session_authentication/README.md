<-- Session Authentication -->
In Rest Api session authentication is done by the client sending his/her credential over the internet to the server and the server confirming that the user(
client) matches the credentials. Since REST is stateless the server cannot save
r have memory of the state of the client.

The credential are first bit 64 encoded in order to ensure backwords compatibility do that non-printable characters are not lost during transmission.
