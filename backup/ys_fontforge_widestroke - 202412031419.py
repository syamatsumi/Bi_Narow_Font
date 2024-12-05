#!fontforge --lang=py -script

import fontforge
import psMat

from .ys_fontforge_Remove_artifacts import ys_rm_little_line, ys_rm_small_poly
from .ys_fontforge_Repair_Self_Intersections import ys_repair_Self_Insec
from .ys_fontforge_tryfix import ys_closepath, ys_repair_si_chain, ys_rescale_chain, ys_simplify



# ���ɂ��炵�ĕ����L����
def ys_widepaste(rwidth, rheight, glyph):

    # ���̃O���t���o�b�N�A�b�v
    glyph_backup = [contour for contour in glyph.foreground]

    for i in range(rwidth)
        

    # ���炵���O���t��ۑ�
    glyph.transform(psMat.translate(rwidth14, 0))
    glyph_tscopy1 = [contour for contour in glyph.foreground]
    glyph.transform(psMat.translate(rwidth14, 0))
    glyph_tscopy2 = [contour for contour in glyph.foreground]
    glyph.transform(psMat.translate(rwidth14, 0))
    glyph_tscopy3 = [contour for contour in glyph.foreground]
    glyph.transform(psMat.translate(rwidth14, 0))
    glyph_tscopy4 = [contour for contour in glyph.foreground]
    glyph.foreground = fontforge.layer()
    
    # �ۑ����Ă����p�X�̏����߂�
    for contour in glyph_backup:
        glyph.foreground += contour

    # �����`�̃T�C�Y���`
    rect_width = rwidth
    rect_height = rheight + rwidth / 2

    for contour in glyph.foreground:
        # �R���^�[�̕������`�F�b�N�i���v���̓X�L�b�v�j
        if contour.isClockwise():
            continue

        ymax = None
        ymin = None

        # ymax��ymin�̒l��������
        max_y = float('-inf')
        min_y = float('inf')

        # �I���J�[�u�|�C���g��T��
        for point in contour:
            if not point.on_curve:
                continue
            if point.y > max_y:
                max_y = point.y
                ymax = point
            if point.y < min_y:
                min_y = point.y
                ymin = point

        # ymax�̃I���J�[�u�|�C���g�����݂���ꍇ
        if ymax:
            # ��������_�Ƃ��钷���`��ǉ�
            pen = glyph.glyphPen(replace=False)

            # �|�C���g��ǉ�
            pen.moveTo(0, 0)
            pen.lineTo(rect_width, 0)
            pen.lineTo(rect_width, rect_height)
            pen.lineTo(0, rect_height)
            pen.closePath()
            pen = None
            glyph.changed = True

            # �V�����ǉ������R���^�[���擾
            rect_contour = glyph.foreground[-1]

            # �����`��z�u�i�ړ��j
            rect_contour.transform(psMat.translate( ymax.x, ymax.y - rect_height))
            print(f"\r now:{glyph.glyphname:<15} kaketa        \r", end=" ", flush=True)

        # ymin�̃I���J�[�u�|�C���g�����݂���ꍇ
        if ymin:
            # ���������_�Ƃ��钷���`��ǉ�
            pen = glyph.glyphPen(replace=False)

            # �|�C���g��ǉ�
            pen.moveTo(0, 0)
            pen.lineTo(rect_width, 0)
            pen.lineTo(rect_width, rect_height)
            pen.lineTo(0, rect_height)
            pen.closePath()
            pen = None
            glyph.changed = True

            # �V�����ǉ������R���^�[���擾
            rect_contour = glyph.foreground[-1]

            # �����`��z�u�i�ړ��j
            rect_contour.transform(psMat.translate( ymin.x, ymin.y))
            print(f"\r now:{glyph.glyphname:<15} kaketa        \r", end=" ", flush=True)


    # ���炵���O���t�ƍ���
    for contour in glyph_tscopy1:
        glyph.foreground += contour
    for contour in glyph_tscopy2:
        glyph.foreground += contour
    for contour in glyph_tscopy3:
        glyph.foreground += contour
    for contour in glyph_tscopy4:
        glyph.foreground += contour

    glyph.round()  # ������
    glyph.removeOverlap()  # ����

    # �E�ɍL�������������S���Y����̂ō��ɂ��炷
    glyph.transform(psMat.translate( - rwidth12 , 0))

    # �S�~�|��
    print(f"\r now:{glyph.glyphname:<15} Cleaning small pieces.         ", end=" ", flush=True)
    ys_rm_little_line(glyph)  # �������ɔ�������2�_�ō\�����ꂽ�p�X(�S�~)���폜
    ys_rm_small_poly(20, 20, glyph)  # �����ȃS�~���폜
    glyph.addExtrema("all") # �ɓ_��ǉ�



# ���X�g���[�N��������
def ys_widestroke(stroke_width, storoke_height, glyph):
    glyph_backup = [contour for contour in glyph.foreground]

    #�S�ẴX�g���[�N�������v���̏ꍇ�t���O����
    is_all_ccw = True
    for contour in glyph.foreground:  # �e�p�X�i�֊s�j�����[�v
        if contour.isClockwise():
            is_all_ccw = False
            break  # 1�ł����v���Ȃ�m�F���I��

    glyph.stroke("elliptical", stroke_width, storoke_height, 0, "round", "miterclip",
        # "circular", width[, CAP, JOIN, ANGLE, KEYWORD],
        # "elliptical", width, minor_width[, ANGLE, CAP, JOIN, KEYWORD],
        # "calligraphic", width, height[, ANGLE, CAP, JOIN, KEYWORD],
        # "convex", contour[, ANGLE, CAP, JOIN, KEYWORD],
        removeinternal=False,  # Default=False (���点����)
        removeexternal=False,  # Default=False (�ׂ点����)
        extrema=False,  # Default=True
        simplify=False,  # Default=True
        removeoverlap="none",  # Default="layer" "contour" "none"
        accuracy=0.5,  # default=0.25
        jlrelative=False,  # Default=True
        joinlimit=0.05,  # Default=20
        ecrelative=True,  # Default=True
        extendcap=0.1,  # Default=0
        arcsclip="ratio"  # Default="auto" "arcs" "svg2" "ratio"
    )

    # ���Ȍ����̏C�����s�B����Ȃ��Ă�2�x�̃c�m�͐܂�B
    ys_repair_si_chain(glyph)

    # ���̃O���t�ƍ���
    ys_rm_small_poly(20, 20, glyph) # �����ȃS�~������
    for contour in glyph_backup:  # �ۑ����Ă����p�X�̏����߂�
        glyph.foreground += contour
    if is_all_ccw:  # ���X�ʏ�p�X(CCW)���������O���t�̏ꍇ
        for contour in glyph.foreground:
            if contour.isClockwise():  # ���]�p�X(CW)�̏ꍇ
                contour.reverseDirection()  # �p�X�𔽓]������
    glyph.removeOverlap()  # ����

    ys_repair_si_chain(glyph) # ������̏C�����s

    # �S�~�|��
    print(f"\r now:{glyph.glyphname:<15} Cleaning small pieces.         ", end=" ", flush=True)
    ys_rm_little_line(glyph)  # 2�_�ō\�����ꂽ�p�X(�S�~)���폜
    ys_rm_small_poly(20, 20, glyph)  # �����ȃS�~���폜
    glyph.addExtrema("all") # �ɓ_��ǉ�



if __name__ == "__main__":
    main()
