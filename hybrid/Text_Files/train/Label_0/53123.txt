
import java.io.*;
import java.util.*;

public class Main {
	
	public static final int MOD = 101;
	
    public static class SegmentTreeNode {
  
        private int val, l, r;
        boolean nextXor;
        SegmentTreeNode left, right;

        public SegmentTreeNode(int[] arr, int l, int r, boolean xor) {
            this.l = l;
            this.r = r;
            this.nextXor = xor;
            if (l == r) {
                this.val = arr[l];
            } else {
                int mid = (l + r) / 2;
                this.left = new SegmentTreeNode(arr, l, mid, !nextXor);
                this.right = new SegmentTreeNode(arr, mid + 1, r, !nextXor);
                if (nextXor) {
                	this.val = right.val ^ left.val;
                } else {
                	this.val = right.val | left.val;
                }
            }
        }

        public int update(int index, int value) {
            if (index < l || index > r) {
                return this.val;
            }

            if (l == index && r == index) {
                this.val = value;
                return this.val;
            }

            if (nextXor) {
            	this.val = right.update(index, value) ^ left.update(index, value);
            } else {
            	this.val = right.update(index, value) | left.update(index, value);
            }
            return this.val;
        }
    }

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int pow = Integer.parseInt(st.nextToken());
        boolean nextXor = pow % 2 == 0;
        int arrSize = (int) Math.pow(2, pow);
        int updateNum = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[arrSize];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arr.length; i++) {
        	arr[i] = Integer.parseInt(st.nextToken());
        }
        
        SegmentTreeNode segTree = new SegmentTreeNode(arr, 0, arr.length - 1, nextXor);
        
        for(int i = 0; i < updateNum; i++) {
        	 st = new StringTokenizer(br.readLine());
        	 int index = Integer.parseInt(st.nextToken());
        	 int val = Integer.parseInt(st.nextToken());
        	 segTree.update(index - 1, val);
        	 System.out.println(segTree.val);
        }
    }
}
