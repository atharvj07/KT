
import java.io.*;
import java.util.ArrayList;
import java.util.Set;
import java.util.TreeMap;

public class _Rough{
        public static void main(String[] args) throws IOException {

            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
            int t = Integer.parseInt(in.readLine());
            while (t-- > 0) {
                String[] s = in.readLine().split(" ");
                int n = Integer.parseInt(s[0]);
                int r = Integer.parseInt(s[1]);

                s = in.readLine().split(" ");
                int[] ar = new int[n];

                for (int i = 0; i < n; i++) {
                    ar[i] = Integer.parseInt(s[i]);
                }

                TreeMap<Integer, Integer> map = new TreeMap<>();
                for (int i = 0; i < n; i++) {
                    map.put(ar[i], 1);
                }
                Set<Integer> list1 = map.keySet();
                ArrayList<Integer> newlist = new ArrayList<>(list1);
                
                int mul = 0;
                int ans = 0;
                for (int i = newlist.size() - 1; i >= 0; i--) {
                    int curr = newlist.get(i);
                    curr -= (mul * r);
                    mul++;
                    if (curr <= 0) {
                        break;
                    } else {
                        ans++;
                    }
                }
                out.write(ans + "\n");
            }
            out.flush();
        }
        }



