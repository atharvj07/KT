import java.util.Scanner;
class Main {
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)) {
			long[] masks = new long[sc.nextInt()];
			for(int i = 0; i < masks.length; i++) {
				int maskLength = sc.nextInt();
				for(int j = 0; j < maskLength; j++) {
					masks[i] += 1L<<sc.nextInt();
				}
			}
			int q = sc.nextInt();
			long flags = 0;

			for(int k = 0; k < q; k++) {
				switch(sc.nextInt()) {
				case 0:
					System.out.println((flags>>sc.nextInt())&1L);
					break;
				case 1:
					flags = flags | masks[sc.nextInt()];
					break;
				case 2:
					flags = flags & ~masks[sc.nextInt()];
					break;
				case 3:
					flags = flags ^ masks[sc.nextInt()];
					break;
				case 4:
					System.out.println((flags|masks[sc.nextInt()])==flags?1:0);
					break;
				case 5:
					System.out.println((flags&~masks[sc.nextInt()])!=flags?1:0);
					break;
				case 6:
					System.out.println((flags&~masks[sc.nextInt()])==flags?1:0);
					break;
				case 7:{
					int cnt = 0;
					int i = sc.nextInt();
					for(int j = 0; j < 64; j++) {
						if(((masks[i]>>j)&1L)>0&&((flags>>j)&1L)>0)
							cnt++;
					}
					System.out.println(cnt);
					break;
				}
				case 8:
					System.out.println(Long.toUnsignedString(flags&masks[sc.nextInt()]));
					break;
				}
			}
		}
	}
}
