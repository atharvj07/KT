
import java.util.Arrays;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

public class Main {

	public static void main(String[] args) {

		new Main().run();
	}

	private void run() {
		Scanner scanner = new Scanner(System.in);
		MDT = new int[16][16];
		for (int i = 0; i < 16; i++) {
			for (int j = 0; j < 16; j++) {
				MDT[i][j] = Math.abs(i / 4 - j / 4) + Math.abs(i % 4 - j % 4);
			}
		}
		int[] a = new int[16];
		int zero = -1;
		for (int i = 0; i < 16; i++) {
			a[i] = scanner.nextInt();
			if (a[i] == 0)
				zero = i;
		}
		int md = getMD(a);
		PriorityQueue<Puzzle> pq = new PriorityQueue<Puzzle>();
		Set<Puzzle> set = new HashSet<Puzzle>();
		pq.offer(new Puzzle(a, zero, md, 0));

		while (!pq.isEmpty()) {
			Puzzle p = pq.poll();
			if (p.md == 0) {
				System.out.println(p.cost);
				break;
			}
			int y = p.zero / 4;
			int x = p.zero % 4;
			for (int[] m : move) {
				int ny = y + m[0];
				int nx = x + m[1];
				if (ny < 0 || 4 <= ny || nx < 0 || 4 <= nx)
					continue;
				int[] tmpMap = Arrays.copyOf(p.map, 16);
				int nz = ny * 4 + nx;
				int nmd = p.md;
				nmd -= MDT[nz][p.map[nz] - 1];
				nmd += MDT[p.zero][p.map[nz] - 1];
				swap(tmpMap, p.zero, nz);
				Puzzle np = new Puzzle(tmpMap, nz, nmd, p.cost + 1);
				if (set.contains(np))
					continue;
				set.add(np);
				pq.offer(np);

			}
		}
	}

	private void swap(int[] tmpMap, int zero, int nz) {
		int tmp = tmpMap[zero];
		tmpMap[zero] = tmpMap[nz];
		tmpMap[nz] = tmp;
	}

	int[][] move = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };

	private int getMD(int[] a) {
		int sum = 0;
		for (int i = 0; i < 16; i++) {
			if (a[i] == 0)
				continue;
			sum += MDT[i][a[i] - 1];
		}
		return sum;
	}

	int[][] MDT;

	class Puzzle implements Comparable<Puzzle> {
		int[] map;
		int zero;
		int md;
		int cost;
		int est;

		public Puzzle(int[] map, int zero, int md, int cost) {
			super();
			this.map = map;
			this.zero = zero;
			this.md = md;
			this.cost = cost;
			this.est = cost + md;
		}

		@Override
		public String toString() {
			return "Puzzle [map=" + Arrays.toString(map) + ", zero=" + zero
					+ ", md=" + md + ", cost=" + cost + ", est=" + est + "]";
		}

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + getOuterType().hashCode();
			result = prime * result + Arrays.hashCode(map);
			return result;
		}

		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			Puzzle other = (Puzzle) obj;
			if (!getOuterType().equals(other.getOuterType()))
				return false;
			if (!Arrays.equals(map, other.map))
				return false;
			return true;
		}

		@Override
		public int compareTo(Puzzle o) {
			if (this.est == o.est)
				return o.cost - this.cost;
			return this.est - o.est;

		}

		private Main getOuterType() {
			return Main.this;
		}

	}
}