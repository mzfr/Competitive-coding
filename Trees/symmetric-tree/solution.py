def isMirror(self, ra, rb):
    if ra is None and rb is None:
        return True

    if ra != None and rb != None:
        if ra.val == rb.val:
            return self.isMirror(ra.left, rb.right) and self.isMirror(ra.right, rb.left)


def isSymmetric(self, root: TreeNode):
    return self.isMirror(root, root)
