# Mini-Interpreter

A Lisp-like language interpreter implemented using Object-Oriented Programming paradigms, design patterns, and clean code principles. This mini-interpreter supports a set of expressions as described in the [Problem Description](docs/problem_description.md). 

## Repository Structure

```plaintext
mini-interpreter
├── README.md
├── assets
│   └── architecture                      -> Simplified architecture diagram
├── interpreter                           
│   ├── core                              -> Core Components folder
│   │   ├── language_constructs           -> Language Constructs Component.
│   │   │   ├── containers                
│   │   │   ├── data_types                
│   │   │   ├── functions
│   │   │   └── objects                        
│   │   ├── program_state                 -> The Program State
│   │   │   ├── logger                     
│   │   │   ├── symbol_table              
│   │   │   └── program_state.py          -> Mediator class              
│   │   └── parser                                  
│   └── program_control_flow.py           -> Program Flow Control class          
├── docs
│   ├── problem_description.md            -> Description of the task          
│   ├── structure.md                      -> This file
│   └── blog_01.md                        -> The blog post with interpreter's architecture description  
└── tests
    ├── generated_tests                   -> Folder with generated tests    
    └── generators                        -> Folder with automatic test generators
```

## Architecture Diagram

<p align="center">
  <img src="assets/architecture/InterpreterArchitectureColoredWhiteBackground.svg" alt="Architecture Diagram" width="600">
</p>


## TODO Tasks

- [ ] Write technical blog post about implementation details and design decisions
- [ ] Integrate error processing component
- [ ] Implement automatic test generation and evaluation scripts
- [ ] Implement debug mode/debugger
- [ ] Migrate code to C++ for improved performance

## Acknowledgement

The problem itself is taken from UBS Coding Challenge.
