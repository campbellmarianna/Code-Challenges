# Closures
## A funciton that accesses a variable "outside" itself.

```code
const message = 'The Bitish are coming.';
function sayMessage(){ // The Closure
    alert(message); // Here we have acces to message, even though it's declared outside this function!
}

```

## One useful thing to do with a closure is to create something like an "instance variable" that can change over time and can affect the behavior of a function.

```code
const getUniqueId = (() => {
    let next Generated
})
```