# language-gnu-avr-asm package
Forked from dkatzdev's language-asm-avr.  
Syntax highlighting package for GNU AVR Assembler. 
Updated the compiler directives to the GNU Assembler Version 2.30.0.

Because I always write the opcodes in lower case so I converted them.
If you like you can adapt the script up2lo.py (you'll find it under snippets)accordingly and convert it back to upper case

### Add the following lines to your style-sheet to enjoy the full feature of pseudo opcode highlighting:

```coffee
@import "syntax-variables";

@very-light-gray: #c5c8c6;
@light-gray: #969896;
@gray: #373b41;
@dark-gray: #282a2e;
@very-dark-gray: #1d1f21;

@cyan: #8abeb7;
@blue: #81a2be;
@purple: #b294bb;
@green: #b5bd68;
@red: #cc6666;
@orange: #de935f;
@light-orange: #f0c674;
@yellow: #ffff00;
// style the background color of the tree view
.tree-view {
 // background-color: whitesmoke;
}

// style the background and foreground colors on the atom-text-editor-element itself
atom-text-editor {
 .syntax--meta {
     &.syntax--class {
       color: @light-orange;
     }

     &.syntax--link {
       color: @orange;
     }

     &.syntax--require {
       color: @blue;
     }

     &.syntax--selector {
       color: @blue;
     }

     &.syntax--separator {
       background-color: @gray;
       color: @syntax-text-color;
     }
     &.syntax--preprocessor.syntax--directive {
       color: @red;
     }
     &.syntax--preprocessor.syntax--c-directive {
        color: @yellow;
     }
     &.syntax--preprocessor.syntax--condition {
       //text-decoration: underline;
       color: @orange;
     }
     &.syntax--preprocessor.syntax--definition {
       color: @light-orange;
     }
 }
}
```
