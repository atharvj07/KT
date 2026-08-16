import java.util.*;
public class P081C {
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int A = in.nextInt();
        int B = in.nextInt();
        
        int[] val = new int[N];
        int[] sval = new int[N];
        for (int n = 0; n < N; ++n)
            val[n] = sval[n] = in.nextInt();
        
        Arrays.sort(sval);
        boolean[] assign = new boolean[N];
        
        if (A == B)
        {
            for (int a = 0; a < A; ++a)
                assign[a] = true;
        }
        else if (A > B)
        {
            int midval = sval[A-1];
            int midcount = 0;
            for (int i = A-1; i >= 0 && sval[i] == midval; --i, ++midcount);

            for (int n = 0; n < N; ++n)
            {
                assign[n] = (val[n] < midval);
                if (val[n] == midval && midcount > 0) { assign[n] = true; --midcount; }
            }
        }
        else
        {
            int midval = sval[B-1];
            int midcount = 0;
            for (int i = B-1; i >= 0 && sval[i] == midval; --i, ++midcount);

            for (int n = N-1; n >= 0; --n)
            {
                assign[n] = !(val[n] < midval);
                if (val[n] == midval && midcount > 0) { assign[n] = false; --midcount; }
            }
        }
        
        for (int n = 0; n < N; ++n)
            System.out.print(assign[n] ? "1 " : "2 ");
        System.out.println();
    }
}
/*

6
5 1
4 4 4 5 4 4

*/
