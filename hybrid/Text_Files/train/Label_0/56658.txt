 import java.util.*;
 public class Main {
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        if(n == 1)
        {
            System.out.println("1");
        }
        else
        {
            int[] arr = new int[n];
            for(int i = 0; i < n; i++)
            {
                arr[i] = s.nextInt();
            }
            ArrayList<Integer> seq = new ArrayList<Integer>();
            int conseq = 1;
            for(int i = 0; i < n - 1; i++)
            {
                if(arr[i] <= arr[i + 1])
                {
                    conseq++;
                    if(i == n - 2)
                        seq.add(conseq);
                }
                else if(arr[i] > arr[i + 1])
                {

                    seq.add(conseq);
                    conseq = 1;
                }
            }
            Collections.sort(seq);

            System.out.println(seq.get(seq.size() - 1));
        }
    }
}