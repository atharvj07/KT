import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class B {

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int n = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        boolean[] used = new boolean[n+1];
        ArrayList<Integer> change = new ArrayList<Integer>(n);
        int[] a = new int[n];
        for(int i = 0; i < n; i++)
        {
            int x = Integer.parseInt(st.nextToken());
            if(x > n || used[x])
                change.add(i);
            else
                used[x] = true;
            a[i] = x;
            
        }
        for(int i = 0, j = 1; i < change.size(); i++)
        {
            while(used[j]) j++;
            a[change.get(i)] = j++;
        }
        
        for(int i = 0; i < n - 1; i++)
            sb.append(a[i]+" ");
        sb.append(a[n-1]+"\n");
        
        System.out.print(sb);
    }
}
