import java.io.IOException;
import java.io.InputStream;
import java.util.NoSuchElementException;

class Scanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;

    private boolean hasNextByte() {
        if (ptr < buflen) {
            return true;
        } else {
            ptr = 0;
            try {
                buflen = in.read(buffer);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (buflen <= 0) {
                return false;
            }
        }
        return true;
    }

    private int readByte() {
        return hasNextByte() ? buffer[ptr++] : -1;
    }

    private boolean isPrintableChar(int c) {
        return 33 <= c && c <= 126;
    }

    private void skipUnprintable() {
        while (hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;
    }

    public boolean hasNext() {
        skipUnprintable();
        return hasNextByte();
    }

    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while (isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    public int nextInt() {
        return (int) nextLong();
    }

    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || '9' < b) {
            throw new NumberFormatException();
        }
        while (true) {
            if ('0' <= b && b <= '9') {
                n *= 10;
                n += b - '0';
            } else if (b == -1 || !isPrintableChar(b)) {
                return minus ? -n : n;
            } else {
                throw new NumberFormatException();
            }
            b = readByte();
        }
    }
}

class CursorList<E> {
	public CursorList<E> prev;
	public CursorList<E> next;
	public boolean isEnd;
	E value;

	public CursorList() {
		this.isEnd = true;
		this.prev = null;
		this.next = null;
	}
	private CursorList(CursorList<E> cursor, E x)
	{
		this.isEnd = false;
		this.value = x;
		this.next = cursor;
		if (cursor.prev != null) {
			cursor.prev.next = this;
			this.prev = cursor.prev;
		} else {
			this.prev = null;
		}
		cursor.prev = this;
	}

	public CursorList<E> insert(E x) {
		this.prev = new CursorList<E>(this, x);
		return this.prev;
	}

	public CursorList<E> move(int d) {
		if (d == 0) {
			return this;
		} else if (d > 0) {
			CursorList<E> tmp = this;
			for (int i = 0; i < d; ++i) {
				tmp = tmp.next;
			}
			return tmp;
//			return next.move(d - 1);
		} else {
			CursorList<E> tmp = this;
			for (int i = 0; i < (-d); ++i) {
				tmp = tmp.prev;
			}
			return tmp;
//			return prev.move(d + 1);
		}
	}

	public CursorList<E> erase() {
		if (this.isEnd) return this;

		if (this.prev != null) {
			this.prev.next = this.next;
		}
		this.next.prev = this.prev;
		return this.next;
	}

	public E get() {
		return value;
	}

	public CursorList<E> top() {
		CursorList<E> tmp = this;
		while(tmp.prev != null) {
			tmp = tmp.prev;
		}
		return tmp;
//		if (this.prev != null) {
//			return this.prev.top();
//		} else {
//			return this;
//		}
	}

}


public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner();
		int q = sc.nextInt();
		CursorList<Integer> list = new CursorList<Integer>();
	    for (int i = 0; i < q; ++i)
	    {
	    	int query = sc.nextInt();
	    	switch (query) {
	    	case 0:
	    		int x = sc.nextInt();
	    		list = list.insert(x);
	    		break;
	    	case 1:
	    		int d = sc.nextInt();
	    		list = list.move(d);
	    		break;
	    	case 2:
	    		list = list.erase();
	    		break;
	    	}

	    }
	    list = list.top();
	    while (!list.isEnd) {
	    	System.out.println(list.value);
	    	list = list.move(1);
	    }
	}


}

