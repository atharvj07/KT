// package com.company;
 import java.io.*;import java.util.*;
 public class Main{
     public static void main(String[] args){
         Scanner s=new Scanner(System.in);
       int n=s.nextInt();long min,max;
       int l=s.nextInt();int r=s.nextInt();
       min=(long)Math.pow(2,l)-1;
       min+=(n-l);
       max=(long)Math.pow(2,r)-1;
       max+=Math.pow(2,r-1)*(n-r);
         System.out.println(min+" "+max);
     }
 }