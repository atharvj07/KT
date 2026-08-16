import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        StringBuilder ans = new StringBuilder();
        while (t-->0) {
            int n = Integer.parseInt(reader.readLine());
            StringTokenizer sToken = new StringTokenizer(reader.readLine());
            ArrayList<Integer> list = new ArrayList<>();
            for (int i=0; i<n; i++) list.add(Integer.parseInt(sToken.nextToken()));
            int rest = n-1;
            for (int i=1; i<=n; i++) {
                int ind = -1;
                for (int j=0; j<list.size(); j++) {
                    if (list.get(j)==i) {
                        ind = j; break;
                    }
                }
                if (ind==-1) continue;
                if (ind<=rest) {
                    rest-=ind;
                    ans.append(i).append(" ");
                    list.remove(ind);
                    for (int j=0; j<ind-1; j++) {
                        ans.append(list.remove(0)).append(" ");
                    }
                    if (rest==0) {
                        for (int elem:list) ans.append(elem).append(" ");
                    }
                } else {
                    int len = list.size();
                    for (int j=0; j<len-1-rest; j++) {
                        ans.append(list.get(j)).append(" ");
                    }
                    ans.append(list.get(len-1)).append(" ");
                    for (int j=len-1-rest; j<len-1; j++) {
                        ans.append(list.get(j)).append(" ");
                    }
                    rest = 0;
                }
                if (rest==0) break;
            }
            ans.append("\n");
        }
        System.out.println(ans);
    }
}