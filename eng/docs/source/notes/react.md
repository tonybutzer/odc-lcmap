## Learning React

### NPM

**Crash Course**
[NPM Crash Course](https://www.youtube.com/watch?v=jHDhaSSKmB0)

React

React is the newest kid on the block 

I’ve been told its super simple to pick up but quickly gets complicated if you’re not careful. 



[https://devchat.tv/react-native-radio/](https://devchat.tv/react-native-radio/)

React Native Radio — if you haven’t given DevChat.tv a visit, you really should. 



[https://www.youtube.com/playlist?list=PLoYCgNOIyGABj2GQSlDRjgvXtqfDxKm5b](https://www.youtube.com/playlist?list=PLoYCgNOIyGABj2GQSlDRjgvXtqfDxKm5b)

React Rapid Course (YouTube) — this is one of the most comprehensive and complete beginner’s courses on YouTube that covers React.



https://leanpub.com/the-road-to-learn-react

The Road to learn React — This is a great field guide if you’re not sure where to begin when it comes to learning React. 



https://www.youtube.com/playlist?list=PLuNEz8XtB51KthRFiVtI8cmXNL9qlQJ5U

Build App with React — Live Coding Series (YouTube)— It’s good to do a code along, especially if you’re new to a particular framework. This lets you see how other people are coding and gives you a comparison to where you are with your skills.



https://krasimir.gitbooks.io/react-in-patterns/content/

React In Patterns — This is a great book to read. Everything in code is made up of patterns. Expose yourself to common React patterns to speed up your workflow.



https://www.fullstackreact.com/30-days-of-react/

30 days of React — If you’re after an easy to understand and digest guide, then give 30 days of React a go. The content is geared towards absolute beginners.



### 30 Days of React

[https://www.fullstackreact.com/30-days-of-react/](https://www.fullstackreact.com/30-days-of-react/)





#### Day 1

[React](https://facebook.github.io/react/) is a JavaScript library for building user interfaces. It is the view layer for web applications.

At the heart of all React applications are **components**.

For example, take a form. A form might consist of many interface 
elements, like input fields, labels, or buttons. Each element inside the
form can be written as a React component. We'd then write a 
higher-level component, the form component itself. 

**React** operates not directly on the browser's Document Object Model (DOM) immediately, but on a **virtual DOM**.



#### JSX



- ES5 (the `ES` stands for ECMAScript) is basically "regular JavaScript."
- ES6 is a new version of JavaScript that adds some nice syntactical and functional additions. It was finalized in 2015. ES6 is [almost fully supported](http://kangax.github.io/compat-table/es6/) by all major browsers.



**JavaScript eXtension**, or more commonly **JSX**, is a React extension that allows us to write JavaScript that *looks like* HTML.

- jsx looks like HTML; - this can be confusing on first glance



combining the view with the functionality makes reasoning about the view straight-forward.



[https://www.fullstackreact.com/30-days-of-react/day-2/](https://www.fullstackreact.com/30-days-of-react/day-2/)



### Note - cntl-B with an html file in sublime

does a build - launches chrome and your off and running



## Day 3 - Our First Component

1. **Babel** is a library for transpiling ES6 to ES5.


```html
<script type="text/babel">
```

> This signals to Babel that we would like it to handle the execution of the JavaScript inside this `script`
> body, this way we can write our React app using ES6 JavaScript and be 
> assured that Babel will **live-transpile** its execution in browsers that 
> only support **ES5**.



[https://semaphoreci.com/community/tutorials/testing-react-components-with-enzyme-and-mocha](https://semaphoreci.com/community/tutorials/testing-react-components-with-enzyme-and-mocha)



1. enzyme
2. Mocha



src is here:

[https://github.com/markthethomas/react-testing-components-enzyme](https://github.com/markthethomas/react-testing-components-enzyme)



## Distraction 1 - Running Js

1. google chrome dev tools;  **Ctrl + Shift + C** OR **F12.**
2. node 
3. npm test with mocha and enzyme
4. code in a simple html



