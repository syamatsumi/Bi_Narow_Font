#!fontforge --lang=py -script

import fontforge

from .ys_fontforge_Repair_Self_Intersections import ys_repair_Self_Insec
from .ys_fontforge_Remove_artifacts import ys_rm_small_poly
from .ys_fontforge_Remove_artifacts import ys_rm_little_line
from .ys_fontforge_Remove_artifacts import ys_rm_small_poly
from .ys_fontforge_tryfix import ys_closepath
from .ys_fontforge_tryfix import ys_simplify
from .ys_fontforge_tryfix import ys_rescale_chain

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

    # ���̃O���t�ƍ���
    if glyph.validate(1) & 0x01:  # �J�����p�X�����o
        ys_closepath(glyph)  # �p�X����違���̑�����
    ys_rm_little_line(glyph)  # 2�_�ō\�����ꂽ�p�X(�S�~)���폜
    ys_repair_Self_Insec(glyph, 1)  # 1�x�ȉ��̊p�x�̓_���ړ�
    if glyph.validate(1) & 0x20:  # �܂����Ȍ���������
        ys_repair_Self_Insec(glyph, 2)  # 2�x�ȉ��̊p�x�̓z��ׂ��B
        if glyph.validate(1) & 0x20:
            ys_repair_Self_Insec(glyph, 3)
            if glyph.validate(1) & 0x20:
                ys_repair_Self_Insec(glyph, 4)
                if glyph.validate(1) & 0x20:
                    ys_repair_Self_Insec(glyph, 5)
                    if glyph.validate(1) & 0x20:
                        ys_repair_Self_Insec(glyph, 6)

    ys_rm_small_poly(20, 20, glyph) # �����ȃS�~������
    for contour in glyph_backup:  # �ۑ����Ă����p�X�̏����߂�
        glyph.foreground += contour
    if is_all_ccw:  # ���X�ʏ�p�X(CCW)���������O���t�̏ꍇ
        for contour in glyph.foreground:
            if contour.isClockwise():  # ���]�p�X(CW)�̏ꍇ
                contour.reverseDirection()  # �p�X�𔽓]������
    glyph.removeOverlap()  # ����

    # �C�����s
    if glyph.validate(1) & 0x01:
        ys_closepath(glyph)
    if glyph.validate(1) & 0x20:
        ys_repair_Self_Insec(glyph, 1) 
        if glyph.validate(1) & 0x20:
            ys_repair_Self_Insec(glyph, 2)
            if glyph.validate(1) & 0x20:
                ys_repair_Self_Insec(glyph, 3)
                if glyph.validate(1) & 0x20:
                    ys_repair_Self_Insec(glyph, 4)
                    if glyph.validate(1) & 0x20:
                        ys_repair_Self_Insec(glyph, 5)
                        if glyph.validate(1) & 0x20:
                            ys_repair_Self_Insec(glyph, 6)
        glyph.removeOverlap()  # ����

    # �S�~�|��
    ys_rm_little_line(glyph)  # 2�_�ō\�����ꂽ�p�X(�S�~)���폜
    ys_rm_small_poly(20, 20, glyph)
    glyph.addExtrema("all") # �ɓ_��ǉ�



if __name__ == "__main__":
    main()
