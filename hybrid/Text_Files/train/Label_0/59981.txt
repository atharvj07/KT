import java.util.Scanner;
public class problem {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] number = new int[100000];
        int[] array = new int[100000];
        int[] time = new int[100000];
        int i,j,n,min,sum,x=0;
        n = input.nextInt();
        for(i=0;i<n;i++){
            number[i] = input.nextInt();
        }
        for(i=0;i<n;i++){
            sum=0;
            for(j=0;j<number[i];j++){
                array[j] = input.nextInt();
                sum+= array[j]*5;
                if(j==number[i]-1)sum+=number[i]*15;
            }
            time[x] = sum;
            x++;
        }
        min = time[0];
        for(x=0;x<n;x++){
            if(min>time[x])min = time[x];
        }
        System.out.println(min);
   }
}
