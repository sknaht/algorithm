import java.util.ArrayList;

class Main {

    public int test(String S) {

        int result = 0;

        String currentpath = "";

        int i = 0;
        int currentlevel = 0;

        boolean[] currentfoldercounted = {false, false, false, false};

        while (i < S.length()) {
            char c = S.charAt(i);

            int level = 0;
            while (c == ' ') {

                level += 1;

                c = S.charAt(++i);
            }

            while (level < currentlevel) {
                currentpath = currentpath.substring(0, currentpath.lastIndexOf('/'));
                currentlevel--;
            }

            currentlevel = level;

            boolean isfolder = true;


            String currentfile = "";
            String extension = "";

            while (c != '\n') {

                if (c == '.') {
                    isfolder = false;
                    extension = "";
                }
                currentfile += c;
                extension += c;
                c = S.charAt(++i);
            }
            i++;

            if (isfolder) {
                currentpath += "/" + currentfile;
                currentlevel++;
                currentfoldercounted[currentlevel] = false;

            } else {
                if (!currentfoldercounted[currentlevel])
                    if (extension.equals(".jpeg") || extension.equals(".png")) {
                        result += currentpath.length();
                        currentfoldercounted[currentlevel] = true;
                    }
            }

        }

        return result;

    }

    /*
    327. Count of Range Sum
    https://leetcode.com/problems/count-of-range-sum/
     */
    public int countRangeSum(int[] nums, int lower, int upper) {
        class TreeNode {
            int countbigger;
            int countself;
            long number;
            TreeNode left, right;

            TreeNode(long number) {
                this.countbigger = 0;
                this.countself = 1;
                this.left = null;
                this.right = null;
                this.number = number;
            }
        }

        class Tree {
            TreeNode root = null;

            public void insert(long number) {
                if (root == null) {
                    root = new TreeNode(number);
                    return;
                }
                TreeNode p = root;
                TreeNode parent = null;
                while (p != null) {
                    parent = p;
                    if (number < p.number)
                        p = p.left;
                    else if (number > p.number) {
                        p.countbigger++;
                        p = p.right;
                    } else {
                        p.countself++;
                        return;
                    }
                }
                if (number < parent.number)
                    parent.left = new TreeNode(number);
                else
                    parent.right = new TreeNode(number);
            }

            public int query(long number) {
                TreeNode p = root;
                int s = 0;
                while (p != null) {
                    if (number <= p.number) {
                        s += p.countbigger + p.countself;
                        p = p.left;
                    } else
                        p = p.right;
                }
                return s;
            }
        }

        Tree tree = new Tree();
        long s = 0;
        int y1 = 0;
        int y2 = 0;
        lower--;

        for (int i = 0; i < nums.length; i++) {
            long x = nums[i];
            tree.insert(s);
            s += x;
            y1 += tree.query(s - lower);
            y2 += tree.query(s - upper);
        }

        return y2 - y1;

    }


    public static void main(String[] args) {

        Main test = new Main();
        String s = "dir1\n dir2\n  pic.jpeg\n  dir3\n   pic.jpeg\n  dir4\n   pic.jpeg";
        test.countRangeSum(new int[]{-2147483647, -2147483648, -1, 0}, -2, 2);
    }

}
/*

"dir1 \n dir2 \n  pic.jpeg \n  dir3 \n   pic.jpeg \n  dir4 \n   pic.jpeg"
 */