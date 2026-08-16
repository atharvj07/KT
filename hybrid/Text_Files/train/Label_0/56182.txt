import java.io.*;
import java.util.*;

public class Solution{ 

	
 public static void main(String[] args) {
     
     Scanner in = new Scanner(System.in);
     
     int n,i,count=0,max=0,answer=0,length=0;
     boolean open=false,word=false;
     
     String w;
     
     n=in.nextInt()+2;
     w=in.next();
     w="_"+w+"_";
     
     
    
     
     for(i=0;i<n;i++){
    	 if(w.charAt(i)=='('){
    		 if(word && length>max)max=length;
    		 length=0;
    		 word=false;
    		 open=true;
    	 }
    	 else if(w.charAt(i)==')'){
    		 if(word){
    			 answer++;
    		 }
    		 length=0;
    		 word=false;
    		 open=false;
    	 }
    	 else if(w.charAt(i)>='a' && w.charAt(i)<='z'){
    		 word=true;
    		 length++;
    	 }
    	 else if(w.charAt(i)>='A' && w.charAt(i)<='Z'){
    		 word=true;
    		 length++;
    	 }
    	 else{
    		 if(open && word){
    			 answer++;
    			 word=false;
    		 }
    		 else if(open&& !word){
    			 
    		 }
    		 else if(!open && word){
    			 if(length>max)max=length;
    			 length=0;
    		 }
    		 else if(!open && !word){
    		 }
    	 }
     }
     
     System.out.println(max+" "+answer);
     
     
     
 }
}