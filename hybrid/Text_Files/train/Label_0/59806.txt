import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) {
      int n=0;
      Scanner s = new Scanner(System.in);
      n=s.nextInt();
      int A[]= new int[n];
      long count4=0;
      long count8=0;
      long count15=0;
      long count16=0;long count23=0;long count42=0;
      int flag=0;
      int count=0;
      for(int i=0;i<n;i++){
        A[i]=s.nextInt();
        if(A[i]==4){
          count4++;
          continue;
        }
        if(A[i]==8){
          if(count4-count8>0){
            count8++;
            continue;
          }
          else{
            count++;
          }
        }
        if(A[i]==15){
          if(count8-count15>0){
            count15++;
            continue;
          }
          else{
            count++;
          }   
        }
        if(A[i]==16){
        if(count15-count16>0){
            count16++;
            continue;
          }
          else{
            count++;
          }
        }
        if(A[i]==23){
        if(count16-count23>0){
            count23++;
            continue;
          }
          else{
            count++;
          }
        }
        if(A[i]==42){
        if(count23-count42>0){
            count8--;count4--;count15--;count16--;count23--;
            continue;
          }
          else{
            count++;
          }
        }
      }
      System.out.println((count4+count8+count15+count16+count23+count42+count));
            
}
}

