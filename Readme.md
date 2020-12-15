### QHexEdit is a binary editor widget for Qt.

It is a simple editor for binary data, just like QPlainTextEdit is for text data.

QHexEdit takes the data of a QByteArray (setData()) and shows it. You can use the mouse or the keyboard to navigate
inside the widget. If you hit the keys
(0..9, a..f) you will change the data. Changed data is highlighted and can be accessed via data().

Normally QHexEdit works in the overwrite mode. You can set overwrite mode(false)
and insert data. In this case the size of data() increases. It is also possible to delete bytes (del or backspace), here
the size of data decreases.

You can select data with keyboard hits or mouse movements. The copy-key will copy the selected data into the clipboard.
The cut-key copies also but deletes it afterwards. In overwrite mode, the paste function overwrites the content of the (
does not change the length) data. In insert mode, clipboard data will be inserted. The clipboard content is expected in
ASCII Hex notation. Unknown characters will be ignored.

QHexEdit comes with undo/redo functionality. All changes can be undone, by pressing the undo-key (usually ctr-z). They
can also be redone afterwards. The undo/redo framework is cleared, when setData() sets up a new content for the editor.
You can search data inside the content with indexOf()
and lastIndexOf(). The replace() function is to change located subdata. This
'replaced' data can also be undone by the undo/redo framework.

QHexEdit is based on QIODevice, that's why QHexEdit can handle big amounts of data. The size of edited data can be more
then two gigabytes without any restrictions.