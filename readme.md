![](images/fw_bot_bck.jpeg)

<h1><center><u>Find, Identify, Monitor and Move Sorter</u></center></h1>
<h2><center>A BOT to do this.</center></h2>
<section>
The file sorter project is built with a responsibility to programmatically move files to destinations
based on a configuration.
</section>

![Static Badge](https://img.shields.io/badge/python-%3E%3Dv3.10-blue)
![Static Badge](https://img.shields.io/badge/dependencies-up_to_date-green)
![Static Badge](https://img.shields.io/badge/dist-download-pink)
![Static Badge](https://img.shields.io/badge/release-v1.0.0-purple)

```flow
st=>start: Login
op=>operation: Login operation
cond=>condition: Successful Yes or No?
e=>end: To admin

st->op->cond
cond(yes)->e
cond(no)->op
```
