import java.util.*;
import java.io.*;

public class Main{
    private final static String[] local = {"5 3\n" +
            "4 3 4 1 6\n" +
            "RROWW","5 2\n" +
            "10 20 14 20 11\n" +
            "RRRRR","11 5\n" +
            "5 6 3 2 3 4 7 5 4 5 6\n" +
            "RWOORWORROW","",""};

    static class Task {

        private void solve() {
            int n = ni(), k = ni();
            int[] b = na(n);
            char[] input = ns().toCharArray();
            int cnt1 = 0, cnt2 = 0, cnt3 = 0;
            ArrayList<Integer> list1 = new ArrayList<>();
            ArrayList<Integer> list3 = new ArrayList<>();
            int max0 = 0, maxr = 0, maxw = 0;
            for (int i = 0; i < n; ++i) {
                char c = input[i];
                if (c == 'R') {
                    cnt1++;
                    list1.add(b[i]);
                    maxr = Math.max(maxr, b[i]);
                }
                else if (c == 'O') {
                    cnt2++;
                    max0 = Math.max(b[i], max0);
                }
                else {
                    cnt3++;
                    list3.add(b[i]);
                    maxw = Math.max(maxw, b[i]);
                }
            }
            if (cnt2 == 0 || ((cnt1 + cnt2 < k) && (cnt2 + cnt3) < k) || (cnt1 == 0 && cnt3 == 0) || k <= 1 ) {
                out.println(-1);
                return;
            }
            for (int i = 0; i < list1.size(); ++i) {
                if (list1.get(i) == maxr) {
                    list1.remove(i);
                    break;
                }
            }
            for (int i = 0; i < list3.size(); ++i) {
                if (list3.get(i) == maxw) {
                    list3.remove(i);
                    break;
                }
            }
            debug(list1);
            debug(list3);
            boolean flag = false;
            for (int i = 0; i < n; ++i) {
                if (input[i] != 'O') continue;
                if (b[i] == max0 && !flag) {
                    flag = true;
                } else {
                    list1.add(b[i]);
                    list3.add(b[i]);
                }
            }
            debug(maxr);
            debug(maxw);
            debug(list1);
            debug(list3);
            if (cnt1 + cnt2 >= k && cnt2 + cnt3 >= k) {
                out.println(Math.max(get(list1, max0 + maxr, k - 2), get(list3, max0 + maxw, k - 2)));
            } else if (cnt1 + cnt2 >= k) {
                out.println(get(list1, max0 + maxr, k - 2));
            } else {
                out.println(get(list3, max0 + maxw, k - 2));
            }
        }

        int get(ArrayList<Integer> list, int init, int k) {
            int ans = init;
            Collections.sort(list);
            Collections.reverse(list);
            Iterator<Integer> it1 = list.iterator();
            for (int i = 0; i < k; ++i)
                ans += it1.next();
            return ans;
        }

        void run(String INPUT, boolean oj){this.oj=oj;out=new PrintWriter(System.out);inputStream = oj ? System.in : new ByteArrayInputStream(INPUT.getBytes());long startTime=System.currentTimeMillis();solve();out.flush();long endTime=System.currentTimeMillis();debug(endTime - startTime + "ms");}
        private InputStream inputStream;private PrintWriter out;private boolean oj;private byte[] inbuf=new byte[1024];private int lenbuf=0,ptrbuf=0;
        private int readByte(){if(lenbuf == -1)throw new RuntimeException();if(ptrbuf>=lenbuf){ptrbuf=0;try{lenbuf=inputStream.read(inbuf);}catch(IOException e){throw new RuntimeException();}if(lenbuf<=0) return -1;}return inbuf[ptrbuf++]; }
        private boolean isSpaceChar(int c){return !(c>=33&&c<=126);}private int skip(){int b;while((b=readByte())!=-1&&isSpaceChar(b));return b;}
        private int[] na(int n){int[] a = new int[n]; for(int i = 0; i < n; ++i) a[i] = ni(); return a;}
        private double nd(){return Double.parseDouble(ns());}private char nc(){return (char)skip();}private int ni(){return Integer.parseInt(ns());}private long nl(){return Long.parseLong(ns());}
        private String ns(){int b = skip();StringBuilder sb = new StringBuilder();while (!(isSpaceChar(b))) {sb.appendCodePoint(b);b = readByte();}return sb.toString(); }
        private int debugCnt = 0;private void debug(Object... o){if(!oj) System.out.println("debug:"+ ++debugCnt + " " + Arrays.deepToString(o));}
    }
    public static void main(String[] args){
        boolean oj = System.getProperty("ONLINE_JUDGE") != null;
        //boolean oj = true;
        if(oj)new Task().run(null, true);else{int test = 1;for(String aLocal : local){if(aLocal.equals(""))continue;System.out.println("Test" + test++ + ":");new Task().run(aLocal,false);}}
    }
}