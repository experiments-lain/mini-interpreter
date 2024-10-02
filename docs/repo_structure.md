# Repo Structure

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
│   └── report_01.md                      -> The blog post with interpreter's architecture description  
└── tests
    ├── generated_tests                   -> Folder with generated tests    
    └── generators                        -> Folder with automatic test generators
```