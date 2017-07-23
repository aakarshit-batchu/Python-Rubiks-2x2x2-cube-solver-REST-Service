#Python Rubiks 2x2x2 Cube Solver REST Servcie

## Introduction:
This a Python REST Service which takes the scrambled color code pattern through JSON request and returns and Optimal Solution to Solve the 2x2x2 Rubiks cube in a JSON response. The Code Outputs the Solution using only the Right(R), Front(F) and Up(U) faces.

R' - Turn Right Anti-Clockwise
R -  Turn Right Clockwise

//Sameways for Up and Front Also

## Installations:
1. python 2.7.12
2. Also the packages used in the program

## To Run the Service:

To start the RESTful Service run the below command:

```
python rubiks2x2x2.py -p 7771 -l /opt/logs
```

```
Flags:
-p or --port The Port on which the Service should Run.
-l or --log  The Path to Directory in which the Logs are to stores.(Logs are stored in a file restservice-rubiks2x2x2.log in the specified directory)
```

## Logging & Monitoring:

REST Service Logs are stored into a file restservice-rubiks2x2x2.log in the specified directory through flag.

## EndPoints:

/two - The JSON Request should be sent to the Endpoint /two.

## Input Scrambled Pattern:

Consider the Layout to be

```
- -   a b   - -   - -
- -   c d   - -   - -

e f   g h   i j   k l
m n   o p   q r   s t

- -   u v   - -   - -
- -   w x   - -   - -
```

The input will be given in the format:
```
abcdefghijklmnopqrstuvwx
```

abcd - will make the Upper Face
efmn - will make the Left Face
ghop - will make the Front Face
ijqr - will make the Right Face
klst - will make the Back Face
uvwx - will make the Bottom Face

There will be six unique characters representing each color, and they can vary, you can use any combination of 6 ascii characters for each color.

## Sample JSON:

You need to post the JSON to the Service with a Key word "pattern" and the value should be the Scrambled Pattern Code.

```
Example:
{"pattern":"GYBOOWRBYGOWGOBRYBYRWGWR"}
```

## Test Results:

Request: curl -XPOST "http://localhost:7771/two" -d '{"pattern":"GYBOOWRBYGOWGOBRYBYRWGWR"}' (Assuming the Service is Running on localhost and port 7771)

Result:  {"Solution": "U'F'U'R2U R2U'R ", "Result": "success"}

## Author:

   NAGA SAI AAKARSHIT BATCHU (aakarshit.batchu@gmail.com)

