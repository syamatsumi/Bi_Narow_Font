#!fontforge --lang=py -script

import fontforge

from .ys_fontforge_Remove_artifacts import ys_rm_little_line, ys_rm_small_poly
from .ys_fontforge_Repair_Self_Intersections import ys_repair_Self_Insec

# �J�����p�X����āA�����Ȃ��p�X���̂Ă�֐�
def ys_closepath(glyph):
    # �p�X������ꂽ�R���^�[��OK�p�X�ϐ��Ƀu�`���ށA
    ok_paths = [contour.dup() for contour in glyph.foreground if contour.closed]
    # �p�X���J�����R���^�[(�������ۑ��ł��ĂȂ��R���^�[)��NG�ϐ��Ƀu�`����
    ng_paths = [contour.dup() for contour in glyph.foreground if contour not in ok_paths]
    # �t�H�A�O���E���h���N���A���āANG�p�X�ϐ��ɓ���Ă��R���^�[�������߂�
    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
    for contour in ng_paths:  # NG�p�X�̏����߂�
        glyph.foreground += contour
    # �J�����p�X����鑀��
    for contour in glyph.foreground:
        contour.addExtrema("all")
        contour.closed = True  # �����I�ɕ���

    # �����I�ɕ��邱�Ƃ��ł����p�X��OK�p�X�ϐ��Ƀu�`���ށA
    ok_paths += [contour.dup() for contour in glyph.foreground if contour.closed]
    glyph.foreground = fontforge.layer()  # �܂��c���Ă�S�~�͒��߂ă|�C�B
    for contour in ok_paths:  # OK�p�X�������߂�
        glyph.foreground += contour
    
    glyph.addExtrema("all")



def ys_repair_si_chain(glyph, proc_cnt):
    if glyph.validate(1) & 0x01:  # �J�����p�X�����o
        print(f"\r now:{glyph.glyphname:<15} Anomality Repair cntclose \r", end=" ", flush=True)
        ys_closepath(glyph)  # �p�X����違���̑�����
    ys_rm_little_line(glyph)  # 2�_�ō\�����ꂽ�p�X(�S�~)���폜

    # �����߂��p�̃o�b�N�A�b�v���擾
    glyph.round()  # ������
    stroke_backup = [contour.dup() for contour in glyph.foreground]

    if glyph.validate(1) & 0x20:  # ���Ȍ���������
        print(f"\r now:{proc_cnt:<5}:{glyph.glyphname:<15} Anomality Repair 1        \r", end=" ", flush=True)
        ys_repair_Self_Insec(glyph, 1)
        glyph.round()
        glyph.removeOverlap()

        if glyph.validate(1) & 0x20:
            print(f"\r now:{proc_cnt:<5}:{glyph.glyphname:<15} Anomality Repair 2        \r", end=" ", flush=True)
            glyph.foreground = fontforge.layer()
            for contour in stroke_backup:
                glyph.foreground += contour
            ys_repair_Self_Insec(glyph, 3)
            glyph.round()
            glyph.removeOverlap()

            if glyph.validate(1) & 0x20:
                print(f"\r now:{proc_cnt:<5}:{glyph.glyphname:<15} Anomality Repair 3        \r", end=" ", flush=True)
                glyph.foreground = fontforge.layer()
                for contour in stroke_backup:
                    glyph.foreground += contour
                ys_repair_Self_Insec(glyph, 4)
                glyph.round()
                glyph.removeOverlap()

                if glyph.validate(1) & 0x20:
                    print(f"\r now:{proc_cnt:<5}:{glyph.glyphname:<15} Anomality Repair 4        \r", end=" ", flush=True)
                    glyph.foreground = fontforge.layer()
                    for contour in stroke_backup:
                        glyph.foreground += contour
                    ys_repair_Self_Insec(glyph, 5)
                    glyph.round()
                    glyph.removeOverlap()

                    if glyph.validate(1) & 0x20:
                        print(f"\r now:{proc_cnt:<5}:{glyph.glyphname:<15} Anomality Repair 5        \r", end=" ", flush=True)
                        glyph.foreground = fontforge.layer()
                        for contour in stroke_backup:
                            glyph.foreground += contour
                        ys_repair_Self_Insec(glyph, 6)
                        glyph.round()
                        glyph.removeOverlap()

                        if glyph.validate(1) & 0x20:
                            print(f"\r now:{proc_cnt:<5}:{glyph.glyphname:<15} Repair failure, rollback. \r", end=" ", flush=True)
                            glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
                            for contour in stroke_backup:  # �ۑ����Ă����p�X�̏����߂�
                                glyph.foreground += contour  # �C�����s�O�ɖ߂�
                            ys_repair_Self_Insec(glyph, 2)
                            glyph.round()
                            glyph.removeOverlap()
    else:
        ys_repair_Self_Insec(glyph, 2)
        glyph.round()
        glyph.removeOverlap()


# �g��k���ɔ����덷�łȂ����Ȃ������s���낵�Ă����̂��
def ys_rescale_chain(glyph):
    glyph_backup = [contour.dup() for contour in glyph.foreground]

    if glyph.validate(1) != 0:  # �ǂꂩ��ł��������������ꍇ
        previous_flags = glyph.validate(1)
        glyph.transform((0.2, 0, 0, 1, 0, 0))
        glyph.round()  # ������
        glyph.addExtrema("all") # �ɓ_��ǉ�
        glyph.removeOverlap()  # ����
        glyph.transform((5, 0, 0, 0.2, 0, 0))
        glyph.round()  # ������
        glyph.addExtrema("all") # �ɓ_��ǉ�
        glyph.removeOverlap()  # ����
        glyph.transform((0.2, 0, 0, 1, 0, 0))
        glyph.round()  # ������
        glyph.addExtrema("all") # �ɓ_��ǉ�
        glyph.removeOverlap()  # ����
        glyph.transform((5, 0, 0, 5, 0, 0))
        current_flags = glyph.validate(1)
        if (previous_flags & ~current_flags) != 0:  # �t���O���u�������v�ꍇ
            pass  # ��������̉��P������ꂽ�̂ŏI���B
        else:
            glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
            for contour in glyph_backup:  # �ۑ����Ă����p�X�̏����߂�
                glyph.foreground += contour  # �C�����s�O�ɖ߂�

        # ���̈����~��
            previous_flags = glyph.validate(1)
            glyph.transform((1, 0, 0, 12.5, 0, 0))
            ys_simplify(glyph)  # �P�������s
            ys_closepath(glyph)  # �J�����p�X�̏C��
            glyph.round()  # ������
            glyph.addExtrema("all") # �ɓ_��ǉ�
            glyph.removeOverlap()  # ����
            glyph.transform((12.5, 0, 0, 0.08, 0, 0))
            ys_simplify(glyph)  # �P�������s
            ys_closepath(glyph)  # �J�����p�X�̏C��
            glyph.round()  # ������
            glyph.addExtrema("all") # �ɓ_��ǉ�
            glyph.removeOverlap()  # ����
            glyph.transform((1, 0, 0, 12.5, 0, 0))
            ys_closepath(glyph)  # �J�����p�X�̏C��
            glyph.round()  # ������
            glyph.addExtrema("all") # �ɓ_��ǉ�
            glyph.removeOverlap()  # ����
            glyph.transform((0.08, 0, 0, 0.08, 0, 0))
            current_flags = glyph.validate(1)
            if (previous_flags & ~current_flags) != 0:  # �t���O���u�������v�ꍇ
                pass  # ��������̉��P������ꂽ�̂ŏI���B
            else:
                glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
                for contour in glyph_backup:  # �ۑ����Ă����p�X�̏����߂�
                    glyph.foreground += contour  # �C�����s�O�ɖ߂�
            # ����Ɏ��̈����~��
                previous_flags = glyph.validate(1)
                glyph.transform((0.25, 0, 0, 1, 0, 0))
                glyph.round()  # ������
                glyph.addExtrema("all") # �ɓ_��ǉ�
                glyph.removeOverlap()  # ����
                glyph.transform((4, 0, 0, 0.25, 0, 0))
                glyph.round()  # ������
                glyph.addExtrema("all") # �ɓ_��ǉ�
                glyph.removeOverlap()  # ����
                glyph.transform((0.25, 0, 0, 1, 0, 0))
                glyph.round()  # ������
                glyph.addExtrema("all") # �ɓ_��ǉ�
                glyph.removeOverlap()  # ����
                glyph.transform((4, 0, 0, 32, 0, 0))
                ys_simplify(glyph)  # �P�������s
                ys_closepath(glyph)  # �J�����p�X�̏C��
                glyph.round()  # ������
                glyph.addExtrema("all") # �ɓ_��ǉ�
                glyph.removeOverlap()  # ����
                glyph.transform((8, 0, 0, 1, 0, 0))
                ys_simplify(glyph)  # �P�������s
                ys_closepath(glyph)  # �J�����p�X�̏C��
                glyph.round()  # ������
                glyph.addExtrema("all") # �ɓ_��ǉ�
                glyph.removeOverlap()  # ����
                glyph.transform((1, 0, 0, 0.125, 0, 0))
                ys_simplify(glyph)  # �P�������s
                ys_closepath(glyph)  # �J�����p�X�̏C��
                glyph.round()  # ������
                glyph.addExtrema("all") # �ɓ_��ǉ�
                glyph.removeOverlap()  # ����
                glyph.transform((0.125, 0, 0, 1, 0, 0))
                current_flags = glyph.validate(1)
                if (previous_flags & ~current_flags) != 0:  # �t���O���u�������v�ꍇ
                    pass  # ��������̉��P������ꂽ�̂ŏI���B
                else:
                    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
                    for contour in glyph_backup:  # �ۑ����Ă����p�X�̏����߂�
                        glyph.foreground += contour  # �C�����s�O�ɖ߂�



# �P�����ɂ�鎩�Ȍ����̏������s
def ys_simplify(glyph):
    # �P�����̐ݒ�Bignoreextrema �� setstarttoextremum ��L����
    flags = ["ignoreextrema", "setstarttoextremum", "smoothcurves", "mergelines", "removesingletonpoints"]  

    ys_rm_small_poly(glyph, 20, 20) # ���ݑ|���֐�
    # ���Ȍ��������p�X��NG�p�X�ϐ��Ƀu�`����(�V�K)
    ng_paths = [contour.dup() for contour in glyph.foreground if contour.selfIntersects()]
    # ���Ȍ������ĂȂ��p�X(�������ۑ��ł��ĂȂ��R���^�[)��OK�ϐ��Ƀu�`����(�V�K)
    ok_paths = [contour.dup() for contour in glyph.foreground if contour not in ng_paths]
    # �t�H�A�O���E���h���N���A���āANG�p�X�ϐ��ɓ���Ă��R���^�[�������߂�
    glyph.foreground = fontforge.layer() # �t�H�A�O���E���h���N���A
    for contour in ng_paths:  # NG�p�X�̏����߂�
        glyph.foreground += contour
        contour.addExtrema("all")
    glyph.simplify(0.05, flags)  # �P�����Ŏ���΂�����
    ys_rm_small_poly(glyph, 20, 20) # ���ݑ|���֐�
    
    for contour in glyph.foreground:# ���̑���ŊJ�����p�X����鑀��
        if not contour.closed:  # �J�����p�X���ǂ������m�F
            contour.addExtrema("all")
            contour.closed = True  # �����I�ɕ���

    # ���Ȍ��������p�X��NG�p�X�ϐ��Ƀu�`����(�V�K)
    ng_paths = [contour.dup() for contour in glyph.foreground if contour.selfIntersects()]
    # ���Ȍ������ĂȂ��p�X(�������ۑ��ł��ĂȂ��R���^�[)��OK�ϐ��Ƀu�`����(�ǋL)
    ok_paths += [contour.dup() for contour in glyph.foreground if contour not in ng_paths]
    glyph.foreground = fontforge.layer() # �܂��c���Ă�S�~�̓|�C�B
    for contour in ok_paths:  # OK�p�X�������߂�
        glyph.foreground += contour
        contour.addExtrema("all")
    
    # �P�����̎Q�l�B
    # [error_bound, flags, tan_bounds, linefixup, linelenmax]
    #"ignoreslopes",  # Allow slopes to change
    #"ignoreextrema",  # Allow removal of extrema
    #"smoothcurves",  # Allow curve smoothing
    #"choosehv",  # Snap to horizontal or vertical
    #"forcelines",  # flatten bumps on lines
    #"nearlyhvlines",  # Make nearly horizontal/vertical lines be so
    #"mergelines",  # Merge adjacent lines into one
    #"setstarttoextremum",  # Rotate the point list so that the start point is on an extremum
    #"removesingletonpoints",  # If the contour contains just one point then remove it



if __name__ == "__main__":
    main()
