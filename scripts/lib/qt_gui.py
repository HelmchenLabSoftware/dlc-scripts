import pandas as pd
import numbers
from PyQt5 import QtGui, QtCore, QtWidgets


def qtable_load_from_pandas(qtable, df, append=False):
    if not append:
        # self.gui.collectionCardsTable.clear()
        qtable.setRowCount(0)

        # Set columns of QTable as DataFrame columns
        qtable.setColumnCount(len(df.columns))
        qtable.setHorizontalHeaderLabels(list(df.columns))

    for idx, row in df.iterrows():
        rowIdxQtable = qtable.rowCount()

        qtable.insertRow(rowIdxQtable)
        for iCol, cell in enumerate(list(row)):
            if isinstance(cell, numbers.Number):
                item = QtWidgets.QTableWidgetItem()
                item.setData(QtCore.Qt.DisplayRole, cell)
            else:
                item = QtWidgets.QTableWidgetItem(str(cell))
            qtable.setItem(rowIdxQtable, iCol, item)

    qtable.resizeColumnsToContents()