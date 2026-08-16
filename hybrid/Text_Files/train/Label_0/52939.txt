import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;

public class Main {
	private long[][] blocks;
	private ArrayList<HashSet<Long>> containList;
	private long[] add;
	private int N, SIZE_OF_BLOCK;

	public void solve() {
		N = nextInt();
		SIZE_OF_BLOCK = (int) Math.sqrt(N);// 1ブロックのサイズ
		int Q = nextInt();
		int[] array = new int[N];
		for (int i = 0; i < N; i++) {
			array[i] = nextInt();
		}

		int BLOCK_NUM = N / SIZE_OF_BLOCK + 1;
		containList = new ArrayList<>();
		for (int i = 0; i < BLOCK_NUM; i++) {
			containList.add(new HashSet<Long>());
		}

		blocks = new long[BLOCK_NUM][SIZE_OF_BLOCK];
		for (int i = 0; i < N; i++) {
			int block = i / SIZE_OF_BLOCK;
			int idx = i % SIZE_OF_BLOCK;
			blocks[block][idx] = array[i];
			containList.get(block).add(blocks[block][idx]);
		}

		add = new long[BLOCK_NUM];

		StringBuilder ans = new StringBuilder();
		for (int q = 0; q < Q; q++) {
			int type = nextInt();
			if (type == 1) {
				// 加算クエリ
				int from = nextInt() - 1;
				int to = nextInt() - 1;
				int addition = nextInt();

				int fromBlock = from / SIZE_OF_BLOCK;
				int toBlock = to / SIZE_OF_BLOCK;
				if (fromBlock == toBlock) {
					if (from % SIZE_OF_BLOCK == 0 && (to + 1) % SIZE_OF_BLOCK == 0) {
						add[fromBlock] += addition;
					} else {
						add2Array(from, to, addition);
					}
					continue;
				}

				if (from % SIZE_OF_BLOCK != 0) {
					add2Array(from, (fromBlock + 1) * SIZE_OF_BLOCK - 1, addition);
					fromBlock++;
				}
				if ((to + 1) % SIZE_OF_BLOCK != 0) {
					add2Array(toBlock * SIZE_OF_BLOCK, to, addition);
					toBlock--;
				}

				for (int i = fromBlock; i <= toBlock; i++) {
					add[i] += addition;
				}
			} else {
				// 検索クエリ
				int target = nextInt();
				int first = -1;
				searchFirst: for (int block = 0; block < BLOCK_NUM; block++) {
					if (containList.get(block).contains(target - add[block])) {
						for (int i = 0; i < SIZE_OF_BLOCK; i++) {
							if (blocks[block][i] + add[block] == target) {
								first = block * SIZE_OF_BLOCK + i;
								break searchFirst;
							}
						}
					}
				}
				if (first == -1) {
					ans.append(-1 + "\n");
					continue;
				}

				int last = first;
				searchLast: for (int block = BLOCK_NUM - 1; block >= 0; block--) {
					if (containList.get(block).contains(target - add[block])) {
						for (int i = SIZE_OF_BLOCK - 1; i >= 0; i--) {
							if (block * SIZE_OF_BLOCK + i >= N) {
								continue;
							}

							if (blocks[block][i] + add[block] == target) {
								last = block * SIZE_OF_BLOCK + i;
								break searchLast;
							}
						}
					}
				}
				ans.append((last - first) + "\n");
			}
		}
		System.out.print(ans.toString());

	}

	private void add2Array(int from, int to, int addition) {
		for (int i = from; i <= to; i++) {
			int block = i / SIZE_OF_BLOCK;
			int idx = i % SIZE_OF_BLOCK;
			blocks[block][idx] += addition;
		}

		int block = to / SIZE_OF_BLOCK;
		containList.get(block).clear();
		for (int i = 0; i < SIZE_OF_BLOCK; i++) {
			if (block * SIZE_OF_BLOCK + i >= N) {
				break;
			}
			blocks[block][i] += add[block];
			containList.get(block).add(blocks[block][i]);
		}
		add[block] = 0;
	}

	private int nextInt() {
		int c;
		try {
			c = System.in.read();
			while (c != '-' && (c < '0' || c > '9'))
				c = System.in.read();
			if (c == '-')
				return -nextInt();
			int res = 0;
			while (c >= '0' && c <= '9') {
				res = res * 10 + c - '0';
				c = System.in.read();
			}
			return res;
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return -1;
	}

	public static void main(String[] args) {
		new Main().solve();
	}
}