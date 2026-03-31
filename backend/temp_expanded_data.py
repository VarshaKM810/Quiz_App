
# Study Materials for each category
MATERIALS_DATA = [
    {
        "category": "html",
        "title": "HTML: The Foundation of the Web",
        "content": """
# HyperText Markup Language (HTML)
HTML is the standard markup language for creating web pages. It describes the structure of a web page semantically.

## Core Concepts & Advanced Features
- **Semantic HTML**: Tags like `<main>`, `<section>`, `<article>`, `<aside>`, and `<nav>` provide meaning to the structure.
- **HTML5 Features**: Native `<audio>` and `<video>` tags, the `<canvas>` element for graphics, and local storage.
- **Forms & Validation**: Input types like `email`, `number`, `range`, and `date` with built-in validation via `required` and `pattern`.
- **Accessibility (A11y)**: Using `alt` text for images, `aria-label`, and proper heading hierarchy (`h1`-`h6`).
- **Head Metadata**: Meta tags for SEO, linking externally to CSS, and Favicons.

```html
<!-- Example of Semantic Structure -->
<header>
  <h1>My Awesome Site</h1>
  <nav><ul><li><a href="/">Home</a></li></ul></nav>
</header>
<main>
  <article>
    <h2>Introduction to HTML</h2>
    <p>Semantic tags help search engines understand your content.</p>
  </article>
</main>
```
        """
    },
    {
        "category": "css",
        "title": "CSS: Styling and Layout",
        "content": """
# Cascading Style Sheets (CSS)
CSS is used to style the layout and appearance of web pages.

## Layout Systems & Styling
- **Flexbox**: 1D layout for rows or columns. Key properties: `flex-direction`, `justify-content`, `align-items`.
- **CSS Grid**: 2D layout for rows AND columns. Key properties: `grid-template-columns`, `grid-gap`, `align-content`.
- **The Box Model**: Understanding `content`, `padding`, `border`, and `margin`. `box-sizing: border-box` is a best practice.
- **Responsive Design**: Using `@media` queries to change styles based on screen width.
- **Variables & Custom Properties**: Defining `--main-color: #333;` and using `var(--main-color)`.
- **Animations**: Using `@keyframes` and the `transition` property for smooth UI effects.

```css
/* Responsive Grid Example */
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

@media (max-width: 600px) {
  body { font-size: 14px; }
}
```
        """
    },
    {
        "category": "js",
        "title": "JavaScript: Making Pages Interactive",
        "content": """
# JavaScript (JS)
JavaScript is a high-level, interpreted scripting language used to create dynamic content.

## Modern JS Features (ES6+)
- **Arrow Functions**: Concise syntax: `const add = (a, b) => a + b;`.
- **Destructuring**: Extracting values from objects/arrays: `const { name } = user;`.
- **Async/Await**: Handling promises cleanly: `const data = await fetch(url);`.
- **The DOM**: Using `querySelector`, `addEventListener`, and `createElement`.
- **Modules**: `export` and `import` for code organization.
- **Closures & Scope**: Understanding Lexical scope and private variables.

```javascript
// Fetching data example
async function getUser() {
  try {
    const response = await fetch('https://api.github.com/users/octocat');
    const user = await response.json();
    console.log(`User: ${user.login}`);
  } catch (error) {
    console.error("Error fetching user:", error);
  }
}
```
        """
    },
    {
        "category": "python",
        "title": "Python: Versatile and Powerful",
        "content": """
# Python
Python is an interpreted, high-level, general-purpose programming language.

## Key Features & Ecosystem
- **Data Collections**: Lists, Sets, Tuples, and Dictionaries (hash maps).
- **List Comprehensions**: Concise list creation: `[x**2 for x in range(10)]`.
- **OOP**: Classes, Inheritance, and the `self` keyword.
- **Standard Library**: Modules like `os`, `sys`, `json`, and `datetime`.
- **Popular Libraries**: `Pandas` for data, `FastAPI`/`Flask` for web, `Pytest` for testing.
- **Virtual Environments**: Using `venv` to manage dependencies.

```python
# Function with Type Hinting
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Dictionary Example
user_data = {"id": 1, "name": "Alice"}
```
        """
    },
    {
        "category": "sql",
        "title": "SQL: Mastering Data",
        "content": """
# Structured Query Language (SQL)
SQL is used for managing and manipulating relational databases.

## Advanced Querying
- **Joins**: `INNER`, `LEFT`, `RIGHT`, and `FULL OUTER`. Understanding how to combine data.
- **Aggregation**: `GROUP BY` with `COUNT(*)`, `SUM()`, `AVG()`.
- **Filtering**: `WHERE` (pre-aggregation) vs `HAVING` (post-aggregation).
- **Subqueries**: Queries within queries for complex filtering.
- **Indexes**: Improving read performance at the cost of write performance.
- **Transactions**: `BEGIN`, `COMMIT`, `ROLLBACK` for data integrity.

```sql
-- Join and Aggregate Example
SELECT users.username, COUNT(orders.id)
FROM users
JOIN orders ON users.id = orders.user_id
WHERE orders.status = 'shipped'
GROUP BY users.username
HAVING COUNT(orders.id) > 5;
```
        """
    },
    {
        "category": "java",
        "title": "Java: Build Once, Run Anywhere",
        "content": """
# Java
Java is a class-based, object-oriented programming language.

## Core Concepts
- **JVM & JRE**: The Java Virtual Machine allows portability across platforms.
- **OOP Principles**: Encapsulation, Abstraction, Inheritance, Polymorphism.
- **Collections Framework**: `ArrayList`, `HashSet`, `HashMap`.
- **Streams API**: Functional processing of data (Java 8+).
- **Multi-threading**: Using `Thread` class or `Runnable` interface.
- **Maven/Gradle**: Build tools for dependency management.

```java
// Streams and Lambda Example
List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
List<String> filteredNames = names.stream()
    .filter(s -> s.startsWith("A"))
    .map(String::toUpperCase)
    .collect(Collectors.toList());
```
        """
    },
    {
        "category": "cpp",
        "title": "C++: High-Performance Systems",
        "content": """
# C++
C++ supports procedural, object-oriented, and generic programming.

## Advanced Systems Programming
- **Memory Management**: Pointers (`*`), References (`&`), and the Stack vs Heap.
- **Smart Pointers**: `std::unique_ptr` and `std::shared_ptr` (modern C++).
- **STL (Standard Template Library)**: `std::vector`, `std::map`, `std::sort`.
- **RAII**: Resource Acquisition Is Initialization - a key pattern for safety.
- **Templates**: Writing generic classes and functions.

```cpp
// Template function example
template <typename T>
T add(T a, T b) {
    return a + b;
}

// Vector usage
std::vector<int> nums = {1, 2, 3};
nums.push_back(4);
```
        """
    },
    {
        "category": "php",
        "title": "PHP: Server-Side Web Scripting",
        "content": """
# PHP
PHP is a popular general-purpose scripting language suited for web development.

## Modern PHP (7.x & 8.x)
- **Typed Properties**: `public string $name;` (PHP 7.4+).
- **PDO**: PHP Data Objects for secure database interactions.
- **Composer**: Dependency manager (like npm for JS).
- **Frameworks**: `Laravel` and `Symfony`.
- **Attributes**: Native metadata (PHP 8.0+).

```php
// PDO Prepared Statement example
$stmt = $pdo->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $userEmail]);
$user = $stmt->fetch();
```
        """
    },
    {
        "category": "react",
        "title": "React: Modern UI Library",
        "content": """
# React
React is a JavaScript library for building user interfaces.

## Hooks & State Management
- **useState**: Managing local component data.
- **useEffect**: Handling side effects (fetching data, subscriptions).
- **useContext**: Passing data without "prop drilling".
- **JSX**: Writing HTML-like syntax inside JS files.
- **Components**: Functional components are the modern standard.
- **Virtual DOM**: Optimized rendering by only updating what changed.

```jsx
// Simple Component with Hook
function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      Count is {count}
    </button>
  );
}
```
        """
    },
    {
        "category": "git",
        "title": "Git & GitHub: Version Control",
        "content": """
# Git and GitHub
Git is the industry-standard version control system for tracking changes.

## Workflow & Collaboration
- **Basic Commands**: `init`, `add`, `commit`, `status`, `push`, `pull`.
- **Branching**: `git branch feature-x`, `git checkout feature-x`.
- **Merging vs Rebasing**: Two ways to integrate changes.
- **GitHub Workflow**: Forks, Pull Requests, and Issues.
- **Merge Conflicts**: Resolving overlapping changes manually.
- **.gitignore**: Excluding files from tracking (e.g., `node_modules`).

```bash
# Typical Feature Workflow
git checkout -b new-feature
# (make changes)
git add .
git commit -m "Add new feature"
git push origin new-feature
```
        """
    },
    {
        "category": "node",
        "title": "Node.js: Server-Side JavaScript",
        "content": """
# Node.js
Node.js allows JS to run on the server, built on Chrome's V8 engine.

## Runtime & Package Management
- **Event Loop**: Highly scalable asynchronous architecture.
- **Express.js**: Fast, unopinionated web framework.
- **NPM**: Installing and managing project dependencies.
- **Buffer/FS**: Low-level access to streams and the file system.
- **Environment Variables**: Using `.env` with `dotenv` for configuration.

```javascript
// Basic Express Server
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000);
```
        """
    },
    {
        "category": "ts",
        "title": "TypeScript: Scalable JavaScript",
        "content": """
# TypeScript
TypeScript adds static types to JavaScript for better tooling and reliability.

## Typing System
- **Interfaces**: Defining object shapes: `interface User { id: number; }`.
- **Union Types**: Allowing multiple types: `let val: string | number;`.
- **Generics**: Reusable components: `function identity<T>(arg: T): T { return arg; }`.
- **Type Guards**: Narrowing types using `typeof` or `instanceof`.
- **Enums**: Set of named constants.

```typescript
// Interface and function example
interface Point {
  x: number;
  y: number;
}

function logPoint(p: Point) {
  console.log(`${p.x}, ${p.y}`);
}
```
        """
    },
    {
        "category": "docker",
        "title": "Docker: Containerization",
        "content": """
# Docker
Docker simplifies application deployment by using containers.

## Images & Containers
- **Dockerfile**: instructions to build an image (`FROM`, `RUN`, `COPY`, `CMD`).
- **Images**: Read-only snapshot of an environment.
- **Containers**: Running instance of an image.
- **Docker Compose**: Orchestrating multi-container apps (e.g., App + DB).
- **Volumes**: Persistent storage outside the container.
- **Network**: Communication between containers.

```dockerfile
# Simple Dockerfile for Node
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```
        """
    },
    {
        "category": "mongodb",
        "title": "MongoDB: NoSQL Database",
        "content": """
# MongoDB
A document-oriented NoSQL database known for high scalability.

## Document Storage & CRUD
- **Collections**: Groups of BSON documents (similar to tables).
- **Documents**: JSON-like data with dynamic schemas.
- **Querying**: Using JSON-based filters: `db.users.find({age: {$gt: 18}})`.
- **Aggregation**: Multi-stage data processing pipeline (`$match`, `$group`, `$sort`).
- **Indexes**: Optimized searching via `createIndex()`.
- **Mongoose**: ODM for Node.js (defines schema in code).

```javascript
// Mongoose Schema Example
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, unique: true },
  age: Number
});
```
        """
    }
]


# Additional Questions to expand the quiz
EXTRA_QUESTIONS = [
    # HTML
    {
        "category": "html",
        "text": "What is the correct way to specify an image source in HTML?",
        "options": [
            {"id": "a", "text": "<img path='image.jpg'>"},
            {"id": "b", "text": "<img src='image.jpg'>"},
            {"id": "c", "text": "<image src='image.jpg'>"},
            {"id": "d", "text": "<img href='image.jpg'>"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "html",
        "text": "Which attribute is used to provide an alternative text for an image?",
        "options": [
            {"id": "a", "text": "title"},
            {"id": "b", "text": "alt"},
            {"id": "c", "text": "description"},
            {"id": "d", "text": "caption"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "html",
        "text": "What does the <canvas> element do?",
        "options": [
            {"id": "a", "text": "Display database records"},
            {"id": "b", "text": "Display draggable elements"},
            {"id": "c", "text": "Draw graphics via scripting (usually JavaScript)"},
            {"id": "d", "text": "Create complex tables"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "html",
        "text": "In HTML, which attribute is used to specify that an input field must be filled out?",
        "options": [
            {"id": "a", "text": "validate"},
            {"id": "b", "text": "placeholder"},
            {"id": "c", "text": "required"},
            {"id": "d", "text": "needed"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "html",
        "text": "Which HTML element is used to define semantic navigation links?",
        "options": [
            {"id": "a", "text": "<navigate>"},
            {"id": "b", "text": "<links>"},
            {"id": "c", "text": "<nav>"},
            {"id": "d", "text": "<menu>"}
        ],
        "correct_answer": "c"
    },

    # CSS
    {
        "category": "css",
        "text": "Which CSS property is used to stack elements on top of each other?",
        "options": [
            {"id": "a", "text": "z-index"},
            {"id": "b", "text": "stack-order"},
            {"id": "c", "text": "layer"},
            {"id": "d", "text": "position-index"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "css",
        "text": "What is the correct CSS syntax for making all the <p> elements bold?",
        "options": [
            {"id": "a", "text": "p {text-size:bold;}"},
            {"id": "b", "text": "p {font-weight:bold;}"},
            {"id": "c", "text": "<p style='font-size:bold;'>"},
            {"id": "d", "text": "p {style:bold;}"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "css",
        "text": "How do you make a list that lists its items with squares?",
        "options": [
            {"id": "a", "text": "list-type: square;"},
            {"id": "b", "text": "list-style-type: square;"},
            {"id": "c", "text": "type: square;"},
            {"id": "d", "text": "bullet: square;"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "css",
        "text": "Which property is used to center text in CSS?",
        "options": [
            {"id": "a", "text": "text-align"},
            {"id": "b", "text": "align-content"},
            {"id": "c", "text": "margin-center"},
            {"id": "d", "text": "horizontal-align"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "css",
        "text": "Which property is used to add space between the content and the border?",
        "options": [
            {"id": "a", "text": "margin"},
            {"id": "b", "text": "padding"},
            {"id": "c", "text": "spacing"},
            {"id": "d", "text": "border-width"}
        ],
        "correct_answer": "b"
    },

    # JS
    {
        "category": "js",
        "text": "How do you create a function in JavaScript?",
        "options": [
            {"id": "a", "text": "function:myFunction()"},
            {"id": "b", "text": "function = myFunction()"},
            {"id": "c", "text": "function myFunction()"},
            {"id": "d", "text": "create myFunction()"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "js",
        "text": "How to write a WHILE loop in JavaScript?",
        "options": [
            {"id": "a", "text": "while i = 1 to 10"},
            {"id": "b", "text": "while (i <= 10)"},
            {"id": "c", "text": "while (i <= 10; i++)"},
            {"id": "d", "text": "loop while (i <= 10)"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "js",
        "text": "What is the correct way to stop a event bubbling in JavaScript?",
        "options": [
            {"id": "a", "text": "event.stop()"},
            {"id": "b", "text": "event.preventDefault()"},
            {"id": "c", "text": "event.stopPropagation()"},
            {"id": "d", "text": "event.cancel()"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "js",
        "text": "Which operator is used to assign a value to a variable?",
        "options": [
            {"id": "a", "text": "*"},
            {"id": "b", "text": "-"},
            {"id": "c", "text": "="},
            {"id": "d", "text": "x"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "js",
        "text": "What does JSON stand for?",
        "options": [
            {"id": "a", "text": "JavaScript Object Notation"},
            {"id": "b", "text": "Java Standard Object Network"},
            {"id": "c", "text": "JavaScript Online Node"},
            {"id": "d", "text": "Joint Solution Object Network"}
        ],
        "correct_answer": "a"
    },

    # Python
    {
        "category": "python",
        "text": "Which method can be used to convert a string to lowercase in Python?",
        "options": [
            {"id": "a", "text": "lowerCase()"},
            {"id": "b", "text": "to_lower()"},
            {"id": "c", "text": "lower()"},
            {"id": "d", "text": "lowercase()"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "python",
        "text": "Which keyword is used to create a function in Python?",
        "options": [
            {"id": "a", "text": "func"},
            {"id": "b", "text": "def"},
            {"id": "c", "text": "define"},
            {"id": "d", "text": "function"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "python",
        "text": "Which of these is a valid dictionary in Python?",
        "options": [
            {"id": "a", "text": "{'name': 'Bob', 'age': 25}"},
            {"id": "b", "text": "['name': 'Bob', 'age': 25]"},
            {"id": "c", "text": "('name': 'Bob', 'age': 25)"},
            {"id": "d", "text": "dict['name': 'Bob']"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "python",
        "text": "How do you insert an element at a specific position in a list?",
        "options": [
            {"id": "a", "text": "add()"},
            {"id": "b", "text": "append()"},
            {"id": "c", "text": "insert()"},
            {"id": "d", "text": "push()"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "python",
        "text": "Which operator is used for floor division in Python?",
        "options": [
            {"id": "a", "text": "/"},
            {"id": "b", "text": "//"},
            {"id": "c", "text": "%"},
            {"id": "d", "text": "**"}
        ],
        "correct_answer": "b"
    },

    # SQL
    {
        "category": "sql",
        "text": "How do you select all columns from a table named 'Persons'?",
        "options": [
            {"id": "a", "text": "SELECT [all] FROM Persons"},
            {"id": "b", "text": "SELECT * FROM Persons"},
            {"id": "c", "text": "SELECT Persons"},
            {"id": "d", "text": "GET * FROM Persons"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "sql",
        "text": "How do you select only the records where the 'FirstName' is 'Peter'?",
        "options": [
            {"id": "a", "text": "SELECT * FROM Persons WHERE FirstName='Peter'"},
            {"id": "b", "text": "SELECT [all] FROM Persons WHERE FirstName LIKE 'Peter'"},
            {"id": "c", "text": "SELECT * FROM Persons WHERE FirstName<>'Peter'"},
            {"id": "d", "text": "GET * FROM Persons WHERE Peter"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "sql",
        "text": "How do you select all the records from a table named 'Persons' where the value of the column 'FirstName' starts with an 'a'?",
        "options": [
            {"id": "a", "text": "SELECT * FROM Persons WHERE FirstName='%a%'"},
            {"id": "b", "text": "SELECT * FROM Persons WHERE FirstName='a'"},
            {"id": "c", "text": "SELECT * FROM Persons WHERE FirstName LIKE 'a%'"},
            {"id": "d", "text": "SELECT * FROM Persons WHERE FirstName LIKE '%a'"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "sql",
        "text": "which SQL keyword is used to sort the result-set?",
        "options": [
            {"id": "a", "text": "SORT BY"},
            {"id": "b", "text": "ORDER BY"},
            {"id": "c", "text": "ARRANGE BY"},
            {"id": "d", "text": "SORT"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "sql",
        "text": "How do you return all the records from a table named 'Persons' sorted descending by 'FirstName'?",
        "options": [
            {"id": "a", "text": "SELECT * FROM Persons ORDER BY FirstName DESC"},
            {"id": "b", "text": "SELECT * FROM Persons SORT DESC 'FirstName'"},
            {"id": "c", "text": "SELECT * FROM Persons ORDER FirstName DESC"},
            {"id": "d", "text": "SELECT * FROM Persons SORT 'FirstName' DESC"}
        ],
        "correct_answer": "a"
    },

    # Java
    {
        "category": "java",
        "text": "How do you create a method in Java?",
        "options": [
            {"id": "a", "text": "methodName()"},
            {"id": "b", "text": "void methodName()"},
            {"id": "c", "text": "methodName[]"},
            {"id": "d", "text": "(methodName)"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "java",
        "text": "What is the correct way to create an object in Java?",
        "options": [
            {"id": "a", "text": "ClassName obj = new ClassName();"},
            {"id": "b", "text": "obj = new ClassName();"},
            {"id": "c", "text": "class obj = ClassName();"},
            {"id": "d", "text": "new ClassName obj;"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "java",
        "text": "Which keyword is used to inherit a class in Java?",
        "options": [
            {"id": "a", "text": "implements"},
            {"id": "b", "text": "inherits"},
            {"id": "c", "text": "extends"},
            {"id": "d", "text": "using"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "java",
        "text": "Which keyword is used to create a constant in Java?",
        "options": [
            {"id": "a", "text": "constant"},
            {"id": "b", "text": "final"},
            {"id": "c", "text": "static"},
            {"id": "d", "text": "const"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "java",
        "text": "Which access modifier makes a class member accessible only within its own class?",
        "options": [
            {"id": "a", "text": "public"},
            {"id": "b", "text": "protected"},
            {"id": "c", "text": "private"},
            {"id": "d", "text": "default"}
        ],
        "correct_answer": "c"
    },

    # C++
    {
        "category": "cpp",
        "text": "Which operator is used to access the address of a variable?",
        "options": [
            {"id": "a", "text": "*"},
            {"id": "b", "text": "&"},
            {"id": "c", "text": "$"},
            {"id": "d", "text": "@"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "cpp",
        "text": "Which keyword is used to define a class in C++?",
        "options": [
            {"id": "a", "text": "struct"},
            {"id": "b", "text": "class"},
            {"id": "c", "text": "object"},
            {"id": "d", "text": "define"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "cpp",
        "text": "How do you write a multi-line comment in C++?",
        "options": [
            {"id": "a", "text": "// comment"},
            {"id": "b", "text": "/* comment */"},
            {"id": "c", "text": "# comment"},
            {"id": "d", "text": "-- comment"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "cpp",
        "text": "What is the size of 'int' data type in C++ (usually)?",
        "options": [
            {"id": "a", "text": "2 bytes"},
            {"id": "b", "text": "4 bytes"},
            {"id": "c", "text": "8 bytes"},
            {"id": "d", "text": "1 byte"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "cpp",
        "text": "Which keyword is used to handle exceptions in C++?",
        "options": [
            {"id": "a", "text": "try"},
            {"id": "b", "text": "except"},
            {"id": "c", "text": "catch"},
            {"id": "d", "text": "Both a and c"}
        ],
        "correct_answer": "d"
    },

    # PHP
    {
        "category": "php",
        "text": "Which function is used to get the length of a string in PHP?",
        "options": [
            {"id": "a", "text": "length()"},
            {"id": "b", "text": "strlen()"},
            {"id": "c", "text": "str_len()"},
            {"id": "d", "text": "get_length()"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "php",
        "text": "How do you start a session in PHP?",
        "options": [
            {"id": "a", "text": "session_begin()"},
            {"id": "b", "text": "session_start()"},
            {"id": "c", "text": "start_session()"},
            {"id": "d", "text": "begin_session()"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "php",
        "text": "Which operator is used to concatenate two strings in PHP?",
        "options": [
            {"id": "a", "text": "+"},
            {"id": "b", "text": "."},
            {"id": "c", "text": "&"},
            {"id": "d", "text": "@"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "php",
        "text": "Which superglobal variable holds information about headers, paths, and script locations?",
        "options": [
            {"id": "a", "text": "$_GLOBALS"},
            {"id": "b", "text": "$_SERVER"},
            {"id": "c", "text": "$_ENV"},
            {"id": "d", "text": "$_REQUEST"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "php",
        "text": "How do you create an array in PHP?",
        "options": [
            {"id": "a", "text": "$cars = array('Volvo', 'BMW');"},
            {"id": "b", "text": "$cars = ['Volvo', 'BMW'];"},
            {"id": "c", "text": "Both a and b"},
            {"id": "d", "text": "$cars = (array)'Volvo', 'BMW';"}
        ],
        "correct_answer": "c"
    },

    # React
    {
        "category": "react",
        "text": "How do you write a comment in JSX?",
        "options": [
            {"id": "a", "text": "// comment"},
            {"id": "b", "text": "{/* comment */}"},
            {"id": "c", "text": "<!-- comment -->"},
            {"id": "d", "text": "/* comment */"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "react",
        "text": "What is the purpose of the 'key' prop in React lists?",
        "options": [
            {"id": "a", "text": "To uniquely identify an element among its siblings"},
            {"id": "b", "text": "To style the element"},
            {"id": "c", "text": "To add a database key"},
            {"id": "d", "text": "To bind an event"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "react",
        "text": "Which React Hook is used to perform side effects?",
        "options": [
            {"id": "a", "text": "useState"},
            {"id": "b", "text": "useContext"},
            {"id": "c", "text": "useEffect"},
            {"id": "d", "text": "useReducer"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "react",
        "text": "How many elements can a React component return?",
        "options": [
            {"id": "a", "text": "Only one root element"},
            {"id": "b", "text": "As many as needed"},
            {"id": "c", "text": "Two: one for header, one for body"},
            {"id": "d", "text": "None, it only renders to the DOM"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "react",
        "text": "What is a React Fragment?",
        "options": [
            {"id": "a", "text": "A component that breaks the UI"},
            {"id": "b", "text": "A way to group multiple elements without adding extra nodes to the DOM"},
            {"id": "c", "text": "A piece of state"},
            {"id": "d", "text": "A specialized hook"}
        ],
        "correct_answer": "b"
    },
    # Git
    {
        "category": "git",
        "text": "Which command is used to initialize a new Git repository?",
        "options": [
            {"id": "a", "text": "git start"},
            {"id": "b", "text": "git begin"},
            {"id": "c", "text": "git init"},
            {"id": "d", "text": "git setup"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "git",
        "text": "What does 'git add' do?",
        "options": [
            {"id": "a", "text": "Commits changes to the repository"},
            {"id": "b", "text": "Stages changes for the next commit"},
            {"id": "c", "text": "Creates a new branch"},
            {"id": "d", "text": "Uploads code to GitHub"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "git",
        "text": "How do you create a new branch and switch to it immediately?",
        "options": [
            {"id": "a", "text": "git branch -n <name>"},
            {"id": "b", "text": "git checkout -b <name>"},
            {"id": "c", "text": "git switch new <name>"},
            {"id": "d", "text": "git new-branch <name>"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "git",
        "text": "Which command displays the commit history?",
        "options": [
            {"id": "a", "text": "git history"},
            {"id": "b", "text": "git log"},
            {"id": "c", "text": "git show-commits"},
            {"id": "d", "text": "git past"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "git",
        "text": "What is the purpose of 'git pull'?",
        "options": [
            {"id": "a", "text": "Upload local changes to remote"},
            {"id": "b", "text": "Fetch and merge changes from remote"},
            {"id": "c", "text": "Delete the local repository"},
            {"id": "d", "text": "Change the current branch"}
        ],
        "correct_answer": "b"
    },
    # Node.js
    {
        "category": "node",
        "text": "Which command is used to install all dependencies listed in package.json?",
        "options": [
            {"id": "a", "text": "npm build"},
            {"id": "b", "text": "npm setup"},
            {"id": "c", "text": "npm install"},
            {"id": "d", "text": "npm get"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "node",
        "text": "What is the core engine that Node.js is built upon?",
        "options": [
            {"id": "a", "text": "SpiderMonkey"},
            {"id": "b", "text": "Chakra"},
            {"id": "c", "text": "V8"},
            {"id": "d", "text": "Nitro"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "node",
        "text": "Which built-in module provides file system functionality?",
        "options": [
            {"id": "a", "text": "path"},
            {"id": "b", "text": "fs"},
            {"id": "c", "text": "os"},
            {"id": "d", "text": "http"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "node",
        "text": "In Node.js, what does 'REPL' stand for?",
        "options": [
            {"id": "a", "text": "Run-Eval-Process-Log"},
            {"id": "b", "text": "Read-Eval-Print-Loop"},
            {"id": "c", "text": "Real-time-Event-Processing-Layer"},
            {"id": "d", "text": "Remote-Execution-Programming-Language"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "node",
        "text": "How do you import a module in CommonJS (Node's default)?",
        "options": [
            {"id": "a", "text": "import x from 'module'"},
            {"id": "b", "text": "require('module')"},
            {"id": "c", "text": "include('module')"},
            {"id": "d", "text": "using 'module'"}
        ],
        "correct_answer": "b"
    },
    # TypeScript
    {
        "category": "ts",
        "text": "Which command compiles TypeScript files into JavaScript?",
        "options": [
            {"id": "a", "text": "ts-compile"},
            {"id": "b", "text": "tsc"},
            {"id": "c", "text": "types"},
            {"id": "d", "text": "ts-run"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "ts",
        "text": "Which keyword is used to create a custom type interface?",
        "options": [
            {"id": "a", "text": "interface"},
            {"id": "b", "text": "struct"},
            {"id": "c", "text": "shape"},
            {"id": "d", "text": "model"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "ts",
        "text": "How do you specify that a variable can be either a string or a number?",
        "options": [
            {"id": "a", "text": "let x: string | number"},
            {"id": "b", "text": "let x: string or number"},
            {"id": "c", "text": "let x: string & number"},
            {"id": "d", "text": "let x: any"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "ts",
        "text": "Which keyword defines an optional property in an interface?",
        "options": [
            {"id": "a", "text": "optional"},
            {"id": "b", "text": "?"},
            {"id": "c", "text": "maybe"},
            {"id": "d", "text": "!"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "ts",
        "text": "What is the return type of a function that will never finish executing (e.g. infinite loop)?",
        "options": [
            {"id": "a", "text": "void"},
            {"id": "b", "text": "null"},
            {"id": "c", "text": "never"},
            {"id": "d", "text": "undefined"}
        ],
        "correct_answer": "c"
    },
    # Docker
    {
        "category": "docker",
        "text": "What is a Docker Image?",
        "options": [
            {"id": "a", "text": "A running instance of a container"},
            {"id": "b", "text": "A read-only template used to create containers"},
            {"id": "c", "text": "A server that hosts containers"},
            {"id": "d", "text": "A specialized virtual machine"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "docker",
        "text": "Which instruction in a Dockerfile defines the working directory?",
        "options": [
            {"id": "a", "text": "CD"},
            {"id": "b", "text": "ROOT"},
            {"id": "c", "text": "WORKDIR"},
            {"id": "d", "text": "PATH"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "docker",
        "text": "What does 'docker ps' do?",
        "options": [
            {"id": "a", "text": "Lists all images"},
            {"id": "b", "text": "Lists all running containers"},
            {"id": "c", "text": "Builds a new container"},
            {"id": "d", "text": "Shows system performance"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "docker",
        "text": "How do you map a host port to a container port?",
        "options": [
            {"id": "a", "text": "-p <host>:<container>"},
            {"id": "b", "text": "-m <host>:<container>"},
            {"id": "c", "text": "-port <host>"},
            {"id": "d", "text": "--connect <container>"}
        ],
        "correct_answer": "a"
    },
    {
        "category": "docker",
        "text": "Which Docker Compose command starts all services defined in the file?",
        "options": [
            {"id": "a", "text": "docker-compose start"},
            {"id": "b", "text": "docker-compose up"},
            {"id": "c", "text": "docker-compose build"},
            {"id": "d", "text": "docker-compose run"}
        ],
        "correct_answer": "b"
    },
    # MongoDB
    {
        "category": "mongodb",
        "text": "What kind of database is MongoDB?",
        "options": [
            {"id": "a", "text": "Relational"},
            {"id": "b", "text": "Graph"},
            {"id": "c", "text": "Document-oriented NoSQL"},
            {"id": "d", "text": "Key-value store"}
        ],
        "correct_answer": "c"
    },
    {
        "category": "mongodb",
        "text": "Which terminal command starts the MongoDB shell?",
        "options": [
            {"id": "a", "text": "mongo_shell"},
            {"id": "b", "text": "mongosh"},
            {"id": "c", "text": "dbstart"},
            {"id": "d", "text": "sqlplus"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "mongodb",
        "text": "What is 'BSON'?",
        "options": [
            {"id": "a", "text": "Basic System Object Notation"},
            {"id": "b", "text": "Binary JSON"},
            {"id": "c", "text": "Buffered Scripting Object Network"},
            {"id": "d", "text": "Big Serial Object Node"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "mongodb",
        "text": "Which method is used to update multiple documents at once?",
        "options": [
            {"id": "a", "text": "db.collection.update()"},
            {"id": "b", "text": "db.collection.updateMany()"},
            {"id": "c", "text": "db.collection.modifyAll()"},
            {"id": "d", "text": "db.collection.batchUpdate()"}
        ],
        "correct_answer": "b"
    },
    {
        "category": "mongodb",
        "text": "What field is automatically generated by MongoDB as a primary key?",
        "options": [
            {"id": "a", "text": "id"},
            {"id": "b", "text": "_id"},
            {"id": "c", "text": "key"},
            {"id": "d", "text": "uid"}
        ],
        "correct_answer": "b"
    }
]
