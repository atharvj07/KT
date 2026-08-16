import java.util.*;

public class Result {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args){
        int n = scanner.nextInt();
        int[] a = new int[n];
        int i;
        for (i=0;i<n;i++)
            a[i] = scanner.nextInt();
        int max = n,index=0,posCount=0,negCount=0;
        for (i=0;i<n;i++)
            if (a[i]==max){
                index = i;
                break;
            }

        if (index<n-1)
            posCount=1;
        if (index>0)
            negCount=1;

        for(i=1;i<=n-1;i++){
            if (a[index+posCount]==max-i) {
                if (index + posCount + 1 < n)
                    posCount++;
            }
            else if (a[index-negCount]==max-i) {
                if (index - negCount - 1 >= 0)
                    negCount++;
            }
            else {
                break;
            }
        }
        scanner.close();
        if (i==n)
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}
