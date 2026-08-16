import java.util.Scanner;


public class JavaApplication11 {
    public static void main(String[] args) {
 Scanner in = new Scanner(System.in);
    
    int n = in.nextInt();
    int x = in.nextInt();
    int arr [] = {1,2,3,4,5,6};
    int lastface1 = 0;
    int lastface2 = 0;
    int num1 =0 ;
    int num2 =0 ;
    int num3 = 0 ;
    int num4 = 0 ;
     String result ="YES";       
    
    for (int i = 0 ; i < n ; i++) //O( n )
    {
        lastface1 = 0;
        lastface2 = 0;
      num1 = in.nextInt();
      num2 = in.nextInt();
      num3 = 7 - num1 ;
      num4 = 7 - num2 ;
      
      
      for (int j = 0 ; j < arr.length;j++)
      {
          if(arr[j]!= num1 && arr[j]!= num2 && arr[j]!= num3 && arr[j]!= num4 )
          {
              if(lastface1 == 0)
                  lastface1 = arr[j];
              else
                  lastface2 = arr[j];
          }
      }
      
      if( lastface1!= x && lastface2 != x)
      {
          result = "NO";
      }
      
      
    }
    
    
      System.out.println(result);
    
       }
    
}
