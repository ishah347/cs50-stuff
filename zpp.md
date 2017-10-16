# Z++

## Questions

1.

```
function main()
{
    // Get values of x and y
    $x <- get()
    $y <- get()

    // subtract y from x
    subtract($x, $y)
}

function subtract($a, $b)
{
    $c <- add($a, -$b)
    // return $c, where $c is the result of (x - y)
    return($c)
}
```

2.

```
function main()
{
    // Get values of x and y
    $x <- get()
    $y <- get()

    // multiply x and y
    multiply($x, $y)
}

function multiply($a, $b)
{
    if (0 < $b)
    {
        return(add($a, multiply($a, add($b, -1))))
    }
    if ($b < 0)
    {
        return(add(-$a, multiply($a, add($b, 1))))
    }
    return(0)
}
```

3.

```
function main()
{
    // Get values of x and y
    $x <- get()
    $y <- get()

    // multiply x and y
    multiply($x, $y)
}

function multiply($a, $b)
{
    if (0 < $b)
    {
        return(add($a, multiply($a, add($b, -1))))
    }
    if ($b < 0)
    {
        return(add(-$a, multiply($a, add($b, 1))))
    }
    return(0)
}
```

## Debrief

1. Lecture 3 notes

2. 3 hours
