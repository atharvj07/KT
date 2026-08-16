import java.util.*;
import java.io.*;
public class PoloPenguinAndMatrix {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                arr.add(Integer.parseInt(st.nextToken()));
            }
        }
        Object[] myarr = arr.toArray();
        Arrays.sort(myarr);
        int count = 0;
        for(int i=0; i<myarr.length; i++){
            if(((int)myarr[i] - (int)myarr[myarr.length/2])%d != 0){
                count = -1;
                break;
            }
            else{
                count += Math.abs(((int)myarr[i] - (int)myarr[myarr.length/2])/d);
                // System.out.println(myarr[i] + " - " + myarr[myarr.length/2] + " \\/ " + d);
            }
        }
        System.out.println(count);
    }
}
