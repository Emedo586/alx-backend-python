# Python Async Function

## Asyncio is a Python library that is used for concurrent programming, including the use of async iterator in Python.It is a programming paradigm in Python that allows for the execution of multiple tasks seemingly in parallel. This is particularly useful for IO-bound and high-level structured network code.

<img align="center" width="500" src="https://i.pinimg.com/originals/75/e7/ef/75e7ef7aa27009befb076509382b86b8.gif">

## Where Does Async IO Fit In?

- Parallelism consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

- Concurrency is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

- Threading is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads.
What’s important to know about threading is that it’s better for IO-bound tasks. While a CPU-bound task is characterized by the computer’s cores continually working hard from start to finish, an IO-bound job is dominated by a lot of waiting on input/output to complete.
  
![](https://realpython.com/cdn-cgi/image/width=504,format=auto/https://files.realpython.com/media/Screen_Shot_2018-10-17_at_3.18.44_PM.c02792872031.jpg)

To recap the above, concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. The Python standard library has offered longstanding support for both of these through its multiprocessing, threading, and concurrent.futures packages.
