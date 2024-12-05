#!fontforge --lang=py -script

import fontforge
import math

# �s�p�̃m�[�h���ς��֐��ł��B
# �A�C�f�A�o����������Ă��Ƃ�ChatGPT o1-preview�ɏ����Ė�����܂�܂ŁA
# �����ȂƂ���A�����Ɠ����Ă�̂��悭�킩��񂿂�B

# �����ڂɂ킩��Ȃ��قǏ����Ȏ��Ȍ����͐����s�p�������Ă��܂��B
# ���������ɂƂт����΃c�m�ɂȂ�܂����A
# ���������ɔ�яo���Ă��Ă���͂��яo���ċ���|�C���g�͉s�p�Ȃ̂ł��B
# �����ŁA�{�X�N���v�g�ł͉s�p������Ă���|�C���g����ӏ��Ɋ񂹏W�߂Ă��܂��܂��B
# ���Ƃ�glyph.removeOverlap()�ŏd�������|�C���g���폜����΂����̂ł����A
# �p�X�̌������������ȏ�Ԃ�glyph.removeOverlap()������
# ���̂܂܃O���t�����`���N�`���ɂȂ����Ⴄ�̂ŁA
# ������glyph.removeOverlap()�������Ă��܂���B
# �C�ӂ̃^�C�~���O�Ŏ��{����悤�ɂ��Ă��������B
# �ł���΂�������s�������オ��낵�����Ǝv���܂���B�i�L�́M �j

def ys_repair_Self_Insec(glyph, angle_threshold=2):
    import math
    angle_threshold_rad = math.radians(angle_threshold)

    for contour in glyph.foreground:
        num_points = len(contour)

        # �R���^�[���ɃI���J�[�u�|�C���g�����݂��邩�m�F
        on_curve_exists = any(p.on_curve for p in contour)
        if not on_curve_exists:
            continue  # ���̃R���^�[��

        i = 0
        while i < num_points:
            current_point = contour[i]

            # �p�x�̌v�Z
            if not current_point.on_curve:
                i += 1
                continue  # �I�t�J�[�u�|�C���g�̓X�L�b�v

            # ���̃I���J�[�u�|�C���g��T��
            j = (i + 1) % num_points
            found_next_oncurve = False
            while True:
                if contour[j].on_curve:
                    found_next_oncurve = True
                    break
                j = (j + 1) % num_points
                if j == i:
                    break  # ������Ă��܂����ꍇ

            if not found_next_oncurve:
                i += 1
                continue  # �I���J�[�u�|�C���g��������Ȃ��ꍇ�A����

            next_point = contour[j]

            # �O�̃I���J�[�u�|�C���g��T��
            k = (i - 1) % num_points
            found_prev_oncurve = False
            while True:
                if contour[k].on_curve:
                    found_prev_oncurve = True
                    break
                k = (k - 1) % num_points
                if k == i:
                    break  # ������Ă��܂����ꍇ

            if not found_prev_oncurve:
                i += 1
                continue  # �I���J�[�u�|�C���g��������Ȃ��ꍇ�A����

            prev_point = contour[k]

            # �x�N�g�����v�Z
            vector1 = (current_point.x - prev_point.x, current_point.y - prev_point.y)
            vector2 = (next_point.x - current_point.x, next_point.y - current_point.y)

            # ���ςƊO�ς��v�Z
            dot_product = vector1[0]*vector2[0] + vector1[1]*vector2[1]
            cross_product = vector1[0]*vector2[1] - vector1[1]*vector2[0]

            # �x�N�g���̑傫�����v�Z
            mag1 = math.hypot(*vector1)
            mag2 = math.hypot(*vector2)

            if mag1 > 0 and mag2 > 0:
                # ���ςƊp�x���v�Z
                angle = math.atan2(cross_product, dot_product)
                if angle < 0:
                    angle += 2 * math.pi
            else:
                angle = 0.0  # �x�N�g���̑傫�����[���̏ꍇ

            # �p�x�����̂���ꍇ�̏���
            if angle_threshold_rad < angle < (2 * math.pi - angle_threshold_rad):
                # ���̂Ȃ��p�x�̏ꍇ
                i += 1
                continue
            else:
                # ���̂���p�x�̏ꍇ
                # ���̂���|�C���g�̘A��������
                problem_points = []
                start_idx = i
                max_iterations = num_points  # �������[�v�h�~�̂���
                iterations = 0

                while iterations < max_iterations:
                    problem_points.append(i)
                    i = (i + 1) % num_points
                    iterations += 1

                    if i == start_idx:
                        break  # ��������ꍇ

                    current_point = contour[i]
                    if not current_point.on_curve:
                        continue
                    # ���̃I���J�[�u�|�C���g��T��
                    j = (i + 1) % num_points
                    found_next_oncurve = False
                    while True:
                        if contour[j].on_curve:
                            found_next_oncurve = True
                            break
                        j = (j + 1) % num_points
                        if j == i:
                            break  # ������Ă��܂����ꍇ
        
                    if not found_next_oncurve:
                        i += 1
                        continue  # �I���J�[�u�|�C���g��������Ȃ��ꍇ�A����
        
                    next_point = contour[j]
        
                    # �O�̃I���J�[�u�|�C���g��T��
                    k = (i - 1) % num_points
                    found_prev_oncurve = False
                    while True:
                        if contour[k].on_curve:
                            found_prev_oncurve = True
                            break
                        k = (k - 1) % num_points
                        if k == i:
                            break  # ������Ă��܂����ꍇ
        
                    if not found_prev_oncurve:
                        i += 1
                        continue  # �I���J�[�u�|�C���g��������Ȃ��ꍇ�A����
        
                    prev_point = contour[k]
                    # �x�N�g�����Čv�Z
                    vector1 = (current_point.x - prev_point.x, current_point.y - prev_point.y)
                    vector2 = (next_point.x - current_point.x, next_point.y - current_point.y)

                    dot_product = vector1[0]*vector2[0] + vector1[1]*vector2[1]
                    cross_product = vector1[0]*vector2[1] - vector1[1]*vector2[0]

                    mag1 = math.hypot(*vector1)
                    mag2 = math.hypot(*vector2)

                    if mag1 > 0 and mag2 > 0:
                        angle = math.atan2(cross_product, dot_product)
                        if angle < 0:
                            angle += 2 * math.pi
                    else:
                        angle = 0.0

                    # �p�x�̕]��
                    if angle_threshold_rad < angle < (2 * math.pi - angle_threshold_rad):
                        # ���̂Ȃ��p�x�����ꂽ��I��
                        break

                if iterations >= max_iterations:
                    print("Warning: Potential infinite loop detected in contour processing.")
                    break  # �������[�v��h�~

                # ���̂���|�C���g�̏���
                num_problems = len(problem_points)

                # �n�_�ƏI�_���擾
                start_idx = (problem_points[0] - 1) % num_points
                end_idx = (problem_points[-1] + 1) % num_points
                start_point = contour[start_idx]
                end_point = contour[end_idx]

                if num_problems % 2 == 0:
                    # �����̏ꍇ�A���_�̕��ύ��W���v�Z
                    total_x = sum(contour[p_idx].x for p_idx in problem_points)
                    total_y = sum(contour[p_idx].y for p_idx in problem_points)
                    total_points = num_problems  # ���I���J�[�u�|�C���g��
                    avg_x = total_x / total_points
                    avg_y = total_y / total_points

                    # �n�_�ƏI�_�̍��W�͈͂��擾
                    min_x = min(start_point.x, end_point.x)
                    max_x = max(start_point.x, end_point.x)
                    min_y = min(start_point.y, end_point.y)
                    max_y = max(start_point.y, end_point.y)

                    # ���ύ��W���͈͓��ɂ��邩�̃`�F�b�N
                    x_in_range = min_x <= avg_x <= max_x
                    y_in_range = min_y <= avg_y <= max_y

                    if not x_in_range and not y_in_range:
                        # x����y���̗����Ŕ͈͊O�̏ꍇ�A�n�_�ƏI�_�̒��ԓ_���g�p
                        new_x = (start_point.x + end_point.x) / 2
                        new_y = (start_point.y + end_point.y) / 2
                    else:
                        # �����łȂ��ꍇ�A���ύ��W���g�p
                        new_x = avg_x
                        new_y = avg_y

                else:
                    # ��̏ꍇ�A�n�_�ƏI�_�̒��ԓ_���g�p
                    new_x = (start_point.x + end_point.x) / 2
                    new_y = (start_point.y + end_point.y) / 2

                # �n�_�ƏI�_�ɗאڂ���I�t�J�[�u�|�C���g���ړ��Ώۂ��珜�O
                # �n�_�ɗאڂ���I�t�J�[�u�|�C���g
                start_adjacent_idx = (start_idx + 1) % num_points
                if not contour[start_adjacent_idx].on_curve and start_adjacent_idx in problem_points:
                    problem_points.remove(start_adjacent_idx)

                # �I�_�ɗאڂ���I�t�J�[�u�|�C���g
                end_adjacent_idx = (end_idx - 1) % num_points
                if not contour[end_adjacent_idx].on_curve and end_adjacent_idx in problem_points:
                    problem_points.remove(end_adjacent_idx)

                # ���̂���S�Ẵ|�C���g�i�I�t�J�[�u�|�C���g�܂ށj��V�����ʒu�Ɉړ�
                for p_idx in problem_points:
                    contour[p_idx].x = new_x
                    contour[p_idx].y = new_y
            print(f"\r now:{glyph.glyphname:<15} {i} {p_idx}", end=" ", flush=True)
            i += 1  # ���̃|�C���g�֐i��

if __name__ == "__main__":
    ys_rmSelfInsec(glyph, 2)
