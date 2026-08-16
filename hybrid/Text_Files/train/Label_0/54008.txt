import java.util.Scanner;

public class SpitProblem {

    public static void main(String[] args) {
       Scanner sin = new Scanner(System.in);
       int n = sin.nextInt(), cm[] = new int[n], arr[] = new int[n];
       for(int i = 0; i < n; i++)
       {
           cm[i] = sin.nextInt();
           arr[i] = sin.nextInt() + cm[i];
       }
       
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
               if(cm[j] == arr[i])
                  if(cm[i] == arr[j])
                  {
                      System.out.println("YES");
                      return;
                  }
        System.out.println("NO");
    }
    
}