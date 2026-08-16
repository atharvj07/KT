/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */


import java.util.Scanner;

/**
 *
 * @author $tar
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    
    public int ptr=0;
    public int start=0;
    public static int arr[];
    public static int end=0;
    public static void main(String[] args) {
        // TODO code application logic here
         Scanner sc = new Scanner(System.in);
         String s = sc.nextLine();
        String s1 = sc.nextLine();
        
        String a[] =s1.split(" ");
        end=Integer.parseInt(s)-1;
        arr = new int[Integer.parseInt(s)];
        for(int j=0;j<arr.length;j++){
        arr[j]=Integer.parseInt(a[j]);
        }
       // end=Integer.parseInt(s)-1;
        check(0);
        
        
    }
    
    
    public static void check(int pointer){
        if(pointer>end)
            return;
        
   if(pointer==0){
       if(arr[pointer]>0){
   for(int i =0;i<arr[pointer]-1;i++)
           System.out.print("PRL");
   if(pointer+1<=end)
   {    System.out.print("PR");
        check(pointer+1);
   
   }
       }
       else
       {
       if(end!=0)
               System.out.print("R");
               check(pointer+1);
       }
   
   }
   
   else if(pointer==end)
   {
       if(arr[end]>0){
   for(int i=0;i<arr[end]-1;i++)
       System.out.print("PLR");
       System.out.print("P");
   
       }
   }
   else{
   
   if(arr[pointer]>0){
   
   for(int i=0;i<arr[pointer]-1;i++){
       System.out.print("PLR");
   }
       System.out.print("PR");
       check(pointer+1);
               
   }
   else
   {
   
       System.out.print("R");
       check(pointer+1);
   
   }
   
   
   
   
   }
    
    
    }
    
}
