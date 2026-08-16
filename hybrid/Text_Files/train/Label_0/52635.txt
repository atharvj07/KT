

import java.io.*;
import java.util.*;

public class Slalom {

	public final static int modulo = 1000000007;
	
	public class SegmentTree {
		SegmentTree(int size) {
			int treeSize = biggerPowerOfTwo(size) * 2 - 1;
			updated = new boolean[treeSize];
			tree = new int[treeSize];
			forwardAdd = new boolean[treeSize];
			this.size = size;
			build(0, 0, size - 1);
		}
		
		public void reset(int l, int r) {
			resetRec(0, 0, size - 1, l, r);
		}
		
		public int get(int pos) {
			return getRec(0, 0, size - 1, pos);
		}
		
		public void add(int l, int r, int value) {
			if(value > 0)
				addRec(0, 0, size - 1, l, r, value);
		}
		
		public void print(int[] array) {
			printOrigRec(0, 0, size - 1, array);
		}
		
		@Override
		public String toString() {
			String result = new String();
			int treeSize = biggerPowerOfTwo(size) * 2 - 1;
			for(int i = 0; i < treeSize; ++i) {
				result += tree[i] + " ";
			}
			return result;
		}

		private void printOrigRec(int root, int start, int end, int[] array) {
			if(start == end) {
				array[start] = tree[root];
			} else {
				int mid = mid(start, end);
				forward(root, start, end);
				printOrigRec(left(root), start, mid, array);
				printOrigRec(right(root), mid + 1, end, array);
			}
		}
		
		private void build(int root, int start, int end) {
			tree[root] = 0;
			forwardAdd[root] = false;
			updated[root] = false;
			if(start < end) {
				int mid = mid(start, end);
				build(left(root), start, mid);
				build(right(root), mid + 1, end);
			}
		}
		
		private void resetRec(int root, int start, int end, int l, int r) {
			if(l > end  || r < start) return; // no intersection
			else if(l <= start && end <= r) { // fully contained
				tree[root] = 0; 
				updated[root] = true;
				forwardAdd[root] = false;
			}
			else {
				forward(root, start, end);
				int mid = mid(start, end);
				resetRec(left(root), start, mid, l, r);
				resetRec(right(root), mid + 1, end, l, r);
			}
		}
		
		private int getRec(int root, int start, int end, int pos) {
			if(start == end) {
				return tree[root];
			}
			int mid = mid(start, end);
			forward(root, start, end);
			if(pos <= mid) {
				return getRec(left(root), start, mid, pos);
			}
			else {
				return getRec(right(root), mid + 1, end, pos);
			}
		}
		
		private void addRec(int root, int start, int end, int l, int r, int v) {
			if(l > end  || r < start) return; // no intersection
			else if(l <= start && end <= r) { // fully contained
				addToNode(root, v);
			}
			else {
				forward(root, start, end);
				int mid = mid(start, end);
				addRec(left(root), start, mid, l, r, v);
				addRec(right(root), mid + 1, end, l, r, v);
			}
		}
		
		private void addToNode(int root, int v) {
			if(v > 0) {
				tree[root] = (tree[root] + v) % modulo;
				if(!updated[root]) {
					updated[root] = true;
					forwardAdd[root] = true;
				} // else: if child was updated with ... add -> add more. ... set -> set more 
			}
		}
		
		private void forward(int root, int start, int end) {
			if(start == end) { // leaf
				forwardAdd[root] = false;	
			} else {
				if(updated[root]) {
					if(forwardAdd[root]) {	// add value of root to children
						addToNode(left(root), tree[root]);
						addToNode(right(root), tree[root]);
					} else {			// set value of root to children
						tree[left(root)] = tree[root];
						tree[right(root)] = tree[root];
						tree[root] = 0;
						// children have to set their children as well.
						forwardAdd[left(root)] = false;
						forwardAdd[right(root)] = false;
						updated[left(root)] = true;
						updated[right(root)] = true;
					} 

				}
			}
			tree[root] = 0;
			updated[root] = false;
			forwardAdd[root] = false;
		}
		
		private int left(int root) {
			return 2 * root + 1;
		}
		
		private int right(int root) {
			return 2 * root + 2;
		}
		
		private int mid(int l, int r) {
			return (l+r) / 2;
		}
		
		private int biggerPowerOfTwo(int x) {
			return Integer.highestOneBit(x) << 1;
		}
		
		private int[] tree;
		private boolean[] updated;
		// forwardAdd == true means that the current value has to be added to all children
		// forwardAdd == false means that the current value has to be set to all children
		private boolean[] forwardAdd; 
		
		private int size;
	}
	
	public class Block implements Comparable<Block> {
		int id;
		int x;
		int y1;
		int y2;
		boolean rightBorder;
		
		Block(int id, int x, int y1, int y2, boolean ends) {
			this.id = id;
			this.x = x;
			this.y1 = y1;
			this.y2 = y2;
			this.rightBorder = ends;
		}

		// the order defined here is crucial to the correctness of the algorithm.
		// at a position x: event "end" triggers update until next active block. hence more downwards "ends" have to come first to deactivate a block
		// but all "starts" have to come first as well to activate a block.
		@Override
		public int compareTo(Block o) {
			// first compare x (higher x is smaller), then the one with a right border comes first. if both same direction, then smaller y1 is smaller
			if(this.x == o.x)
				// starting first
				if(this.rightBorder == o.rightBorder) {
					return this.y1 - o.y1; // lower first
				} else {
					if(this.rightBorder) return -1;
					else return +1;
				}
			else
				return o.x - this.x;
		}
	}
	
	public class ActiveBlock implements Comparable<ActiveBlock> {
		int id;
		int topY;
		
		ActiveBlock(int id, int y) {
			this.id = id;
			this.topY = y;
		}

		@Override
		public int compareTo(ActiveBlock o) {
			if(this.topY == o.topY) {
				return this.id - o.id;
			}
			return this.topY - o.topY;
		}
	}
	
	public void solve() throws FileNotFoundException {
		Scanner sc = new Scanner(System.in);
		
//		Scanner sc = new Scanner(new File("Tests/Slalom/27"));
		// input
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();

		Block[] blocks = new Block[2*k+1];
		for(int i = 0; i < k; ++i) {
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			blocks[i] = new Block(i, x2, y1, y2, true);	// as we proceed from right to left, a block "starts" at its right border. 
			blocks[k + i] = new Block(i, x1 - 1 , y1, y2, false); // "ending" blocks are processed _after_ they have ended, so store them at x1 - 1
		}
		blocks[2*k] = new Block(k, n, m-1, m-1, false); //dummy ending block, right of and below (n, m), so stored at (n, m-1)
		Arrays.sort(blocks);
		sc.close();
		
		
		//DEBUG:
//		int[][] matrix = new int[n][m + 2];

		// computation: dynamic programming in matrix
		// value of n, m is 1
		// if getTopRight is blocked, value is sum of getTop and getRight
		// else value is maximum of getTop and getRight
		// space improvement: only store current column of matrix. Use set of blocks to keep track of currently active blocks.
		// time improvement: use segment tree with operations reset(l, r), get(pos) and add(l, r) for this column
		SegmentTree col = new SegmentTree(m + 2);
		col.add(m, m, 1);
		NavigableSet<ActiveBlock> activeBlocks = new TreeSet<ActiveBlock>();
		int i = 0;
		for(int x = n; x >= 1; --x) {
			while((i < 2*k + 1) && blocks[i].x == x) {
				Block curBlock = blocks[i];
				if(curBlock.rightBorder) { // starting blocks
					activeBlocks.add(new ActiveBlock(curBlock.id, curBlock.y2));
					col.reset(curBlock.y1, curBlock.y2);
				} else { // ending blocks
					activeBlocks.remove(new ActiveBlock(curBlock.id, curBlock.y2));
					// all squares left of that block, starting from the y2 of that block to the active next block (search in activeBlocks)
					ActiveBlock lower = activeBlocks.floor(new ActiveBlock(k + 1, curBlock.y2));
					if(lower == null) lower = new ActiveBlock(k + 1, 0);
					if(lower.topY <= curBlock.y2) {
						int value = col.get(curBlock.y2 + 1);
						col.add(lower.topY + 1, curBlock.y2, value);
					}
				}
				++i;
			}
			// DEBUG:
//			col.print(matrix[x-1]);
			
		}

		// DEBUG:
//		for(int Y = m; Y >= 1; Y--) {
//            for(int X = 0; X < n; X++) {
//                System.out.print((matrix[X][Y] < 10 ? " " : "") + matrix[X][Y] + " ");
//            }
//            System.out.println();
//        }

		System.out.println(col.get(1));
	}
	
	public static void main(String[] args) throws IOException {
		new Slalom().solve();
	}

}
