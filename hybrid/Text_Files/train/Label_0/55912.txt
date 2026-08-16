

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigDecimal;
 

 class Main{
             
     public static void main(String args[]){
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         
         try{
             String line;
             while((line=br.readLine())!= null){if(line.isEmpty())break;
                String[] spli=line.split(",");
                
                 int num=Integer.parseInt(spli[0]);
                 double wei=Double.parseDouble(spli[1]);
                 double hig=Double.parseDouble(spli[2]);
                 if(wei/((hig)*(hig))>=25)System.out.println(num);
             }
             
         }catch(Exception e){}         
     }
     
     
    
 }