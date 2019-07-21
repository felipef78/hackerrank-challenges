/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hackerrank;

/**
 *
 * @author Felipe
 */
import java.util.*;
import java.text.*;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

import java.util.*;

class Solution {

    public static void main(String[] argh) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNext()) {
            String input = sc.next();

            if (input.isEmpty()) {
                System.out.println("true");
            } else if (input.length() % 2 != 0) {
                System.out.println("false");
            } else {
                boolean keep =  true;
                Stack<String> s = new Stack<>();
                for (int i = 0; i < input.length(); i++) {                    
                    String st = input.substring(i, i + 1);
                    if (st.equals("{") || st.equals("(") || st.equals("[")) {
                        s.add(st);
                    } else {
                        switch (st) {
                            case ")":
                                if (!s.pop().equals("(")) {
                                    System.out.println("false");
                                    keep = false;
                                }
                                break;
                            case "}":
                                if (!s.pop().equals("{")) {
                                    System.out.println("false");
                                    keep = false;
                                }
                                break;
                            case "]":
                                if (!s.pop().equals("[")) {
                                    System.out.println("false");
                                    keep = false;
                                }
                                break;
                        }
                    }
                    if(!keep){
                        break;
                    }
                }
                if(keep){
                    System.out.println("true");
                }
                s.clear();
            }
        }

    }
}
