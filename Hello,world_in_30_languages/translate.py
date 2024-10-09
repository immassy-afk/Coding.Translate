# Dictionary containing "Hello World" translations for different languages
hello_world_dict = {
    "c": '''#include <stdio.h>
int main() {
    printf("Hello, World!\\n");
    return 0;
}''',
    "cpp": '''#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}''',
    "csharp": '''using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}''',
    "python": '''print("Hello, World!")''',
    "java": '''public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}''',
    "javascript": '''console.log("Hello, World!");''',
    "go": '''package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}''',
    "ruby": '''puts "Hello, World!"''',
    "php": '''<?php
echo "Hello, World!";
?>''',
    "swift": '''print("Hello, World!")''',
    "kotlin": '''fun main() {
    println("Hello, World!")
}''',
    "rust": '''fn main() {
    println!("Hello, World!");
}''',
    "perl": '''print "Hello, World!\\n";''',
    "r": '''cat("Hello, World!\\n")''',
    "haskell": '''main = putStrLn "Hello, World!"''',
    "lua": '''print("Hello, World!")''',
    "dart": '''void main() {
  print('Hello, World!');
}'''
}

def list_languages():
    print("Available languages:")
    for lang in hello_world_dict:
        print(f"- {lang}")

def translate_to(language_code):
    if language_code in hello_world_dict:
        return hello_world_dict[language_code]
    else:
        return "Language not supported."

def main():
    print("Choose which language you want to translate from.")
    print("{Language code} TO {Language code}")
    list_languages()
    
    from_lang = input("\nEnter the language code you want to translate from (default is python): ").strip().lower()
    to_lang = input("Convert python to which language? Enter the language code: ").strip().lower()

    # Default to python if no input is given
    if from_lang == '':
        from_lang = 'python'

    # Check if conversion is from python
    if from_lang != 'python':
        print(f"Translation from {from_lang} to {to_lang} is not supported.")
        return

    print(f"\nTranslating Python 'Hello World' to {to_lang}:\n")
    print(translate_to(to_lang))

if __name__ == "__main__":
    main()
