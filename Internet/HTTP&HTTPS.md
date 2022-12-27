# Internet

---

- **URL**
  
  > **U**niform **R**esource **L**ocator
  > 
  > IP address(example:240.10.20.1) make easy to memorize like example.com

- **Protocol** 
  
  > promised to be followed for communication between computers

- **Router**
  
  > A machine that finds the best path you know and sends packets to the path

- **Packet**
  
  > Data's piece for send data by internet

- **TCP**
  
  > **T**ransmission **C**ontrol **P**rotocol
  > 
  > TCP manages the sending and receiving of all your data as packets

---

## HTTP

> **H**yper **T**ext **T**ransfer **P**rotocol
> 
> The Language used to communicate beween web browsers and servers
> 
> The Language that you use to tell a web browser how to make a page look

if you request one page include images and videos

Images/Videos are separate files with unique urls

the browser sends seperate http response for each of these and displace them as they arrive

- `GET` request
  
  - Your browser send a url and the server response html

- `POST` request
  
  - You send information when you fill out a form or type a search query or login
  
  - how to work
    
    - your browser sends this information in plain text to the web server using an http post request 
    
    - The server your id, password received figures out that who you are
      
      it sends a web page back to your browser,
      
      along with that web page it also attacheds a llittle bit of invisible cookie data
    
    - your browser sees cookie date, save them
      
      - it is important because it's the only way that a website can remember who you are

- Cookie data
  
  - cookie data is id card for website, it's a number that identifies who you are
  
  - your web browser holds on to that number 
  
  - the next time you go the website, your web browser knows to automatically attach that id number with the request it sends over to the server
  
  - the server see the request comming from you browser sees the id number and knows who you are, this is a request from you 



| The Internet                      |
| --------------------------------- |
| Is completely open                |
| The connections are shared        |
| Information is sent in plain text |

this make it possible for hackers to snoop on any personal information that you send over the internet,

but safe websites prevent this by asking your web browser to communicate on a secure channel using something called TLS(= transport layer security) 

A layer of security around your communications

TLS = encryption



### HTTPS

> **H**yper **T**ext **T**ransfer **P**rotoco **S**ecure
> 
> HTTPS ensure that your http requests are secure and protected 
> 
> TLS + HTTP = HTTPS



when a website asks your browser to engage in a secure connection

it first provide a digital certificate which is like an official id card proving that it's request website

digital certificates are published by certificate authorities

Trusted entities that verify identities of websites and issue certificates for them

now if a website tries to start a secure connection without a propertly issued digital certificate your browser will warn you



## Summarize

### HTTP & DNS

> Manage the sending & recieving of web files



what makes this possible?



### TCP/IP & Router network

> break down and transfer information in small packets



how to send packets?



### Wires, cables & Wifi

> binary sequences of 1 and 0 are sent physically
